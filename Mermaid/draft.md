```cpp:
#pragma GCC optimize("O3")
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

constexpr long INF = 1ll << 60;
template <typename T> inline void chmin(T& a, const T& b) {if (a > b) a = b; }
template <typename T> inline void chmax(T& a, const T& b) {if (a < b) a = b; }
template<typename T> inline int sz(const vector<T>&v) { return (int)v.size(); }

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N, M; cin>>N>>M;

  vector<long> A(N); 
  for(auto& e:A) cin>>e;

  vector<int> C(N), indeg(N, 0);
  for(int u=0; u<N; ++u) {
    int v; cin>>v; --v;
    C[u]=v; indeg[v]++;
  }

  vector<bool> init(N, false);
  while(M--) {
    int m; cin>>m; --m;
    init[m]=true;
  }

  long res{};

  vector dp(N, vector<long>(2, -INF));
  vector<vector<pair<long, long>>> child(N);

  queue<int> q;
  for(int s=0; s<N; ++s) if(indeg[s]==0) q.push(s);

  //木の探索
  while(!q.empty()) {
    const auto u=q.front(); q.pop();
    const int v=C[u];

    auto& z=child[u];
    if(z.empty()) {
      if(init[u]) dp[u][true]=A[u];
      else dp[u][false]=0;
    }
    else {
      long sum{};
      bool origin=true;
      //集計 (k>=0)
      for(const auto& [leave, take]:z) {
        sum+=max(take, leave);
        if(origin) origin=leave>take;
      }
      //到達可能である場合の最大値 (k>=1)
      long promised=sum;
      if(origin) {
        promised=-INF;
        for(const auto& [leave, take]:z) chmax(promised, sum-leave+take);
      }

      if(init[u]) {
        dp[u][true]=A[u]+sum;
      }
      else {
        dp[u][false]=A[u]+sum;
        dp[u][true]=A[u]+promised;
      }
    }

    //サイクルを木に分断
    if(u==v) {
      res+=max(dp[u][true], dp[u][false]);
    }
    else {
      //全親ノード探索済の場合のみ呼ばれる?
      child[v].emplace_back(dp[u][true], dp[u][false]);
      if(--indeg[v]==0) q.push(v);
    }
  }

  for(int si=0; si<N; ++si) if(0<indeg[si]) {
    int s=si;
    long best=-INF;
    int source=-1;
  }

  return 0;
}
```
