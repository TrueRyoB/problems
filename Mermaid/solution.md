# Editorial
It is expected to abstract the problem statement into functional graph, a context in graph theory, before designing an implementation.

<details><summary>What is functional graph?</summary>
	It refers to a set of nodes and directed edges where every node has exactly one edge.
	It consists of trees and cycles.
</details>

## Brute force approach
It is possible to solve this problem by testing out all the patterns, costing $O(N2^N)$ runtime complexity.

A certain subset of nodes satisfy the reachability if
1. The set contains $M$ as a subset
2. The breath-first search from initial nodes reaches to every node in the set

The solution is the maximum value of the sum of $A_i$ in across accepted subsets.

This approach is valid for $N \leq 20$.

```cpp:O(2^N) solution
#include <bits/stdc++.h>
using namespace std;
int main() {

	constexpr long INF = 1ll << 60;
	int N, M;
	vector<long> A;
	vector<bool> initialized;
	vector<int> in_deg, C;
	cin >> N;
	A.resize(N), initialized.assign(N, false), in_deg.assign(N, 0), C.resize(N);
	for (auto &x : A) cin >> x;
	for (int i = 0; i < N; i++) {
		cin >> C[i]; C[i]--;
		if (i != C[i]) in_deg[C[i]] += 1;
	}
	cin >> M;
	int base = 0;
	queue<int> queue_base;
	vector d_base(N, false);
	for (int i = 0; i < M; i++) {
		int m;
		cin >> m; m--;
		base |= 1 << m;
		queue_base.push(m);
		d_base[m] = true;
		initialized[m] = true;
	}

	long answer = -INF;
	for (int i = 0; i < 1 << N; i++) if ((base & i) == base) {
		auto bfs_queue = queue_base;
		auto d = d_base;
		while (!bfs_queue.empty()) {
			int u =bfs_queue.front(); bfs_queue.pop();
			int v = C[u];
			if ((i & 1 << v) && !d[v]) d[v] = true, bfs_queue.push(v);
		}

		long tmp{};
		for (int j = 0; j < N; j++)
			if ((i & 1 << j) && !d[j]) tmp = -INF;
			else if (i & 1 << j) tmp += A[j];
		answer = max(answer, tmp);
	}
	cout << answer << endl;
}

```

## Dynamic Programming approach

It is possible to compress irrelevant states of $O(2^N)$ into $O(N)$ owing to the following properties of this problem.
- A value of each node depends only on a set of parent nodes
- The asked operation is monoid.

The entire search process is as follows.
1. BFS on nodes that are guaranteed to be connected
2. BFS on nodes that are not necessarily connected
3. BFS on topologically sorted nodes that takes the maximum valid subset

```cpp:O(N)
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

  //dp[u][k]: the maximum prefix sum by node u if the prefix includes (k) / excludes (!k) u
  vector dp(N, vector<long>(2, -INF));
  vector<vector<pair<long, long>>> child(N);

  queue<int> q;
  for(int s=0; s<N; ++s) if(indeg[s]==0) q.push(s);

  //Tree DP on reachable nodes O(N)
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
      bool cutdown=true;
      //let k be the number of active parent nodes
      //aggregation (k>=0)
      for(const auto& [leave, take]:z) {
        sum+=max(take, leave);
        if(cutdown) cutdown=leave>take;
      }
      //a max value when promised to be connected with initial nodes (k>=1)
      long promised=sum;
      if(cutdown) {
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

    // interrupt the process on a self-loop
    if(u==v) {
      res+=max(dp[u][true], dp[u][false]);
    }
    else {
      child[v].emplace_back(dp[u][true], dp[u][false]);
      if(--indeg[v]==0) q.push(v);
    }
  }

  //Tree DP on semi-reachable nodes for handling a branch merge
  //safe as it is guaranteed for node u be connected with initial nodes if dp[u][true]!=-INF
  vector<int> dealt; dealt.reserve(N);
  for(int u=0; u<N; ++u) if(indeg[u]>0) {
    dealt.push_back(u);
    auto &z=child[u];
    if(z.empty()) {
      dp[u][false]=0;
    } else {
      long sum{};
      bool cutdown=true;
      for(const auto& [leave, take]:z) {
        sum+=max(take, leave);
        if(cutdown) cutdown=leave>take;
      }

      long promised=sum;
      if(cutdown) {
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
  }

  for(const auto& e:dealt) indeg[e]=1;

  //Cut on cycles
  for(int i=0; i<N; ++i) if(0<indeg[i]) {
    int s=i;
    vector<int> cycle={s};
    for(int u=C[s]; u!=s; u=C[u]) cycle.push_back(u);
    for(const auto& e:cycle) indeg[e]=0;

    int sz=(int)cycle.size();
    long dp0=dp[s][false], dp1=dp[s][true], dp2;
    //dp: max prefix sum since s
    //dp0: when excluding u
    //dp1: when including u
    //dp2: when satisfying the reachability from at least one initial node

    auto cycledp = [&]() -> void {
      for(int u=1; u<sz; ++u) {
        int v=cycle[u];

        long nxt0 = dp[v][false]+max(dp0, dp1);
        long nxt1 = max(dp[v][true]+max(dp0, dp1), dp[v][false]+A[v]+dp1);
        long nxt2 = dp2 + max(dp[v][false]+A[v], dp[v][true]);

        if(-INF/2 < dp[v][true]) chmax(nxt2, dp[v][true]+max(dp0, dp1));
        
        dp0=nxt0, dp1=nxt1, dp2=nxt2;
      }
    };

    long best=max(dp0, dp1);
    cycledp();

    dp0=dp2=-INF; dp1=dp[s][false]+A[s];
    cycledp();

    chmax(best, dp2);
    res+=best;
  }
  cout << res << endl;

  return 0;
}
```

## Credit
- [rykazari](https://github.com/rykazari-h): tester
- [RyoB](https://github.com/TrueRyoB): writer
