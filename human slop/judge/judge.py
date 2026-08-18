"""python3

argv[1]: テストケース入力ファイル (N)
argv[2]: テストケース出力ファイル (= train.py が生成した judge_data.txt)
stdin  : 提出解の出力
正常終了 = AC / 例外・assert 失敗 = WA

行数がちょうど N であることは必須。各行を個別に妥当性判定し、
受理された行が ceil(N * RATIO) 行以上であれば AC(重複は2回目以降を不受理として数える)。
"""
import sys
import math
import re

RATIO = 0.7

# ---- 品質フィルタ: 発音可能性(音節パース) + 重子音クラスタの例外白名簿 ----
# 名前を「(頭子音) 母音核 (末子音)」の音節列に分解する。y は母音として扱う(整合)。
# 軽い子音クラスタ(長さ<=2)は一般的合法集合で許可し、重いクラスタ(長さ>=3)は
# 「正しい重構成は少数派(chr は実質 chri- のみ)」という観測に基づき *デフォルト棄却*、
# 実在名コーパスで実証された文脈だけを例外的に許可する(下記白名簿は writer_out から導出)。
# これで str- ジャンク(Strolor)や語中 nstr(Manstrina)を落としつつ、
# Christopher / Tyler / Cynthia 等の合法な重クラスタ実在名は温存する。

# 軽いクラスタ(長さ<=2)用の合法集合。y は母音側で扱うため子音単独からは除外。
_ONSETS = set(['', 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z',
    'bl','br','cl','cr','dr','fl','fr','gl','gr','pl','pr','tr','tw','dw','kr','sc','sk','sl',
    'sm','sn','sp','st','sw','sh','ch','th','wh','ph','gn','kn','wr','qu'])
_CODAS = set(['', 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z',
    'll','nn','ss','tt','ff','dd','ck','ch','sh','th','ng','nk','nt','nd','ns','st','sk','sp',
    'ct','pt','ld','lt','lm','ln','lp','lk','lf','rl','rn','rt','rd','rm','rk','rb','rg','rs','mp','mb','ph'])

# 重クラスタ(長さ>=3)の例外白名簿。実在名(SSA)で実証された構成のみ。
# 語頭は「クラスタ|直後母音の頭文字」で文脈込み(chr|i は可, str|o は不可 で Strolor を棄却)。
_ON_HEAVY = {
    'chl|o', 'chrs|i', 'chr|i', 'chr|o', 'chr|y', 'dhr|u', 'dsh|a', 'khl|o', 'khr|i', 'khr|y',
    'ksh|a', 'mcc|a', 'mcc|o', 'mch|a', 'mck|a', 'mck|e', 'mck|i', 'mck|y', 'mcl|a', 'mcn|e',
    'nth|a', 'phr|o', 'schn|e', 'sch|a', 'sch|e', 'sch|o', 'shl|o', 'shn|e', 'shn|i', 'shr|a',
    'shr|e', 'shr|i', 'shr|u', 'shw|a', 'smr|i', 'sth|e', 'str|a', 'str|e', 'str|i', 'str|y',
    'thr|e', 'thr|i', 'tsh|a',
}
_MED_HEAVY = {
    'chl', 'chr', 'ckl', 'cks', 'ddh', 'ddr', 'ffn', 'ffr', 'ghl', 'ght', 'hnn', 'hnt', 'hsh',
    'ksh', 'lbr', 'ldr', 'lfr', 'llm', 'lls', 'lph', 'lsh', 'lst', 'lth', 'mbl', 'mbr', 'mph',
    'mpl', 'nch', 'ndh', 'ndl', 'ndr', 'nds', 'ndz', 'nfr', 'ngl', 'ngr', 'ngst', 'ngt', 'nnd',
    'nnl', 'nsh', 'nsl', 'nst', 'nth', 'ntl', 'ntr', 'ntw', 'nzl', 'phn', 'phr', 'rch', 'rgr',
    'rkl', 'rld', 'rll', 'rph', 'rrl', 'rsch', 'rsh', 'rst', 'rth', 'rtl', 'rtn', 'rtr', 'sch',
    'shd', 'shk', 'shl', 'shm', 'shn', 'shr', 'sht', 'shv', 'shw', 'ssh', 'ssl', 'ssm', 'sst',
    'sth', 'stl', 'str', 'tch', 'thl', 'thm', 'thn', 'thr', 'thz', 'tth', 'ttl', 'ttn', 'wnd',
    'wndr', 'wnn', 'wnt', 'zzm',
}
_CODA_HEAVY = {
    'cks', 'ghn', 'ght', 'ksh', 'lph', 'nch', 'ndr', 'ndt', 'ngs', 'nsh', 'nth', 'ntz', 'rch',
    'rck', 'rdt', 'rjr', 'rks', 'rld', 'rsh', 'rth', 'rtt', 'stn', 'tch',
}

# ---- 加点式の違反判定 ----
# 「違和感のある名前は存在すべきでない」を前提に、違反ごとに減点を積み、
# 合計が THRESHOLD 以上なら棄却する。各違反の重み:
THRESHOLD  = 1.0
W_STRUCT   = 1.0    # 発音不能(母音なし/軽クラスタ非合法/母音3連超) = 決定的
W_HEAVY    = 1.0    # 実証されない重クラスタ1つ = 決定的(従来ハード相当)
W_WORD_PER = 0.35   # 埋め込み英単語: (語長-3)*これ。 4->0.35, 5->0.70, 6->1.05(単独棄却)

def _longest_embedded_word(s, common):
    """s の部分文字列(長さ>=4)で common(常用英単語)に一致する最長長さ。無ければ0。"""
    n = len(s)
    for L in range(n, 3, -1):
        for i in range(n - L + 1):
            if s[i:i + L] in common:
                return L
    return 0

def demerit(s, common):
    """名前 s の違反スコア(加点)。"""
    d = 0.0
    spans = [(m.start(), m.end()) for m in re.finditer(r'[aeiouy]+', s)]
    if not spans:
        return W_STRUCT + 99     # 母音なし=発音不能
    for a, b in spans:
        if b - a > 3:            # 異常な母音連続(iaeo…)
            d += W_STRUCT
    # 子音クラスタ(語頭/語中/語末): 軽クラスタは合法集合, 重クラスタ(>=3)は白名簿
    lead = s[:spans[0][0]]
    if len(lead) >= 3:
        if (lead + '|' + s[spans[0][0]]) not in _ON_HEAVY:
            d += W_HEAVY
    elif lead not in _ONSETS:
        d += W_STRUCT
    tail = s[spans[-1][1]:]
    if len(tail) >= 3:
        if tail not in _CODA_HEAVY:
            d += W_HEAVY
    elif tail not in _CODAS:
        d += W_STRUCT
    for i in range(len(spans) - 1):
        cluster = s[spans[i][1]:spans[i + 1][0]]
        if len(cluster) >= 3:
            if cluster not in _MED_HEAVY:
                d += W_HEAVY
        elif not any(cluster[:k] in _CODAS and cluster[k:] in _ONSETS
                     for k in range(len(cluster) + 1)):
            d += W_STRUCT
    # 埋め込み英単語(部分文字列として常用語を含む): 語長に比例して加点。
    # 照合先は「常用語(頻度上位) かつ 名前でない(blocklist所属) 4字以上」の COMMON。
    # 全辞書だと leister/doline 等の難語が実在名を誤爆するため常用語に限定する。
    L = _longest_embedded_word(s, common)
    if L >= 4:
        d += W_WORD_PER * (L - 3)
    return d

def quality_ok(s, common):
    return demerit(s, common) < THRESHOLD

def main():
    n_expected = int(open(sys.argv[1]).read().split()[0])

    f = open(sys.argv[2])
    tau = float(f.readline())
    tables = {}
    for _ in range(3):
        tag, cnt = f.readline().split()
        t = {}
        klen = {'T3': 3, 'T2': 2, 'T1': 1}[tag]
        for _ in range(int(cnt)):
            line = f.readline()
            ctx = line[:klen]
            t[ctx] = [float(x) for x in line[klen + 1:].split()]
        tables[tag] = t
    T3, T2, T1 = tables['T3'], tables['T2'], tables['T1']
    tag, cnt = f.readline().split()
    assert tag == 'BLOCK'
    block = set()
    for _ in range(int(cnt)):
        block.add(f.readline().strip())
    tag, cnt = f.readline().split()
    assert tag == 'COMMON'
    common = set()
    for _ in range(int(cnt)):
        common.add(f.readline().strip())

    IDX = {ch: i for i, ch in enumerate('abcdefghijklmnopqrstuvwxyz$')}
    LOWER = set('abcdefghijklmnopqrstuvwxyz')
    UPPER = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    data = sys.stdin.read()
    lines = data.split('\n')
    while lines and lines[-1] == '':
        lines.pop()
    assert len(lines) == n_expected, f'expected {n_expected} lines, got {len(lines)}'

    def valid(name, seen):
        # 形式: ^[A-Z][a-z]{1,14}$
        if not 2 <= len(name) <= 15:
            return False
        if name[0] not in UPPER or not all(c in LOWER for c in name[1:]):
            return False
        s = name.lower()
        if s in seen:
            return False
        seen.add(s)
        # 構造: 文字3連 / bigram3連 / アルファベット昇順4連 の禁止
        if any(s[i] == s[i+1] == s[i+2] for i in range(len(s) - 2)):
            return False
        if any(s[i:i+2] == s[i+2:i+4] == s[i+4:i+6] for i in range(len(s) - 5)):
            return False
        if any(ord(s[i+1]) == ord(s[i]) + 1 and ord(s[i+2]) == ord(s[i]) + 2
               and ord(s[i+3]) == ord(s[i]) + 3 for i in range(len(s) - 3)):
            return False
        # 語彙: SSA 非掲載の英語辞書語は名前と認めない
        if s in block:
            return False
        # 品質: 違反加点が閾値以上(発音不能・非実証の重クラスタ・埋込常用語)なら棄却
        if not quality_ok(s, common):
            return False
        # 統計: 平均対数尤度 >= tau
        buf = '^^^' + s
        tot = 0.0
        for i, ch in enumerate(s + '$'):
            d = T3.get(buf[i:i+3]) or T2.get(buf[i+1:i+3]) or T1[buf[i+2]]
            tot += d[IDX[ch]]
        return tot / (len(s) + 1) >= tau

    seen = set()
    ok = sum(1 for name in lines if valid(name, seen))
    threshold = math.ceil(n_expected * RATIO)
    assert ok >= threshold, f'accepted {ok}/{n_expected} < {threshold}'

main()
