# Editorial: Mermaid

- [rykazari](https://github.com/rykazari-h): tester
- [RyoB](https://github.com/TrueRyoB): writer

The problem asks us to find a subset of nodes with maximum total weight such that every node in the subset is "justified" by a path from a source node $M$ within that same subset.

### 1. Graph Abstraction: The Functional Graph

A **Functional Graph** is a directed graph where every node has exactly one outgoing edge.

* **Structure:** It consists of several connected components. Each component contains exactly one directed cycle, with several trees rooted on the cycle nodes pointing toward the cycle.

### 2. The Reachability Constraint

A subset of nodes $S$ is valid if for every $u \in S$:

1. $u \in M$ (it is a predefined source), OR
2. There exists some $v \in S$ such that $v \to u$ (the predecessor is also in the set).

This means if you pick a node that isn't a source, you **must** pick at least one of its "parents" (nodes pointing to it) to satisfy the reachability requirement.

## Approach 1: Brute Force $O(2^N \cdot N)$

For small $N$ ($N \leq 20$), we can iterate through all $2^N$ possible subsets. For each subset, we check if all nodes are reachable from the intersection of the subset and $M$ using only edges within the subset.

```cpp
inline bool is_valid(int mask) {
	return (mask & source_mask) == mask;
}

```

## Approach 2: Dynamic Programming $O(N)$

Since the graph is a collection of components with one cycle each, we can solve this using **Tree DP** followed by **Cycle DP**.

### Step 1: Tree DP (Topological Sort)

We process the trees pointing towards the cycles starting from the leaves (nodes with in-degree 0).
For a node $u$, let:

* $dp[u][false]$: Max weight of a valid subtree rooted "below" $u$, where $u$ is **not** included.
* $dp[u][true]$: Max weight of a valid subtree rooted "below" $u$, where $u$ **is** included and reachable from a source within its subtree.

**Transitions:**
To compute $dp[u][true]$:

1. If $u \in M$, we can include any optimal subtrees from its parents: $A[u] + \sum \max(dp[p][false], dp[p][true])$.
2. If $u \notin M$, we **must** pick at least one parent $p$ such that $p$ is in the state $dp[p][true]$. If all parents are better off being excluded or are in state $0$, we must force the "least bad" parent to be in state $1$.

### Step 2: Handling the Cycles

After the topological sort, only the cycles remain. Each node on the cycle now has a weight and a "pre-calculated" value from its attached trees.

Because a cycle has a circular dependency, we can't use standard DP. Instead:

1. **Break the cycle:** Pick an arbitrary edge $u \to v$ on the cycle.
2. **Two passes:** * **Case A:** Node $u$ is not included.
* **Case B:** Node $u$ is included (which helps satisfy the reachability of $v$).


3. Run a linear DP around the remaining path.

---

## Optimized Implementation

```cpp
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

### Complexity Analysis

* **Time Complexity:** $O(N)$ because each node and edge is visited a constant number of times during topological sort and cycle traversal.
* **Space Complexity:** $O(N)$ to store the graph and DP states.
