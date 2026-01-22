## Editorial
It is greedy when your decision making is valid regardless of upcoming states.

In this problem, iff an element is a nonnegative number, it is guaranteed to contribute to the maximum value of the substring.


## Sample code (C++17)
~~~:cpp
#pragma GCC optimize("O3")
#include <iostream>

using namespace std;
using ll = long long;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  ll res={0}, u;
  while(cin>>u) if(u>0) res+=u;
  cout<<res<<endl;
  return 0;
}

~~~
