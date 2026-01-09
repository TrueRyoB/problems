## Editorial
Transforming the input into a triangular matrix allows you to calculate a determinant of a given matrix by $O(N^3)$.

Make sure to flip a sign of the result for every row swap and to avoid the overflow.


## Sample code (C++17)
~~~:cpp
#pragma GCC optimize("O3")
#include <vector>
#include <iostream>

using namespace std;
using ll = long long;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N; ll M; cin>>N>>M;

  auto fix = [&](int i, int j) {
    return i*N+j;
  };

  auto mul = [&](ll a, ll b) -> ll {
    return (__int128)a*b%M;
  };

  auto inv = [&](ll t) {
    ll base=t, r=M-2ll, res=1ll;
    while(r) {
      if(r&1) {
        res=mul(res, base);
      }
      base=mul(base, base);
      r>>=1;
    }
    return res;
  };

  vector<ll> mat(N*N);

  for(auto& e:mat) {
    cin>>e; if(e<0) e+=M;
  }

  int sign=1;
  auto swap_row = [&](int a, int b) {
    if(a==b) return;
    sign*=-1;
    for(int j=0; j<N; ++j) swap(mat[fix(a, j)], mat[fix(b, j)]);
  };

  for(int j=0; j<N; ++j) {
    int i=j;
    while(i<N && mat[fix(i, j)]==0) ++i;

    if(i==N) {
      cout << 0 << '\n';
      return 0;
    }
    swap_row(i, j), i=j;
    
    ll base=inv(-mat[fix(i, j)]);
    
    for(int ni=i+1; ni<N; ++ni) if(mat[fix(ni,j)]!=0){
      ll scale=mul(mat[fix(ni,j)], base);
      for(int nj=0; nj<N; ++nj) {
        mat[fix(ni, nj)]+= mul(mat[fix(i,nj)], scale);
        if(mat[fix(ni,nj)]>=M) mat[fix(ni,nj)]-=M;
      }
    }
  }

  ll res=ll{sign};
  for(int i=0; i<N; ++i) res=mul(res, mat[fix(i, i)]);
  cout << res << '\n';

  return 0;
}

~~~
