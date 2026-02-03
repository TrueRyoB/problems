# Scheduling
You have a class pool of $N$ lectures.

Lecture $i$ offers $M_i$ sessions, where session $j$ is held from $t_{i, j, 1}$ to $t_{i, j, 2}$. 

You need to choose exactly one session for enrollment for each lecture.

Determine if it's possible to take all lectures without any time duplications.

## Constraints
- $1 \leq N \leq 18$
- $1 \leq M_i \leq 10$
- $0 \leq t_{i, j, 1} \lt t_{i, j, 2} \leq 10^{10}$


--- 

- 衝突の定義
- minDの設定
- 出力形式の再定義 (数 + 最初のセッション枠を消費)
- 全ソートの手間を解消させるクエリ系の問題設定に

N=6, M=8であれば余裕で間に合う


ただ、すべてに対応できる訳ではない
→
枝切できればうれしい
→
どれからunenrollするか、その意思決定を補助すべき

+ min D
+ 入れれない時間などの設定も出来ればうれしい
