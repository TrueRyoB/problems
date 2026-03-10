# Editorial
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
