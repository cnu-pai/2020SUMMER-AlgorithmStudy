#include <iostream>
using namespace std;
int main() {
 int n;
 long long dp[1001];

  cin >> n;
  dp[0] = 1;
  dp[1] = 1;
  for(int i = 2; i <= n; i++) {
    dp[i] = (dp[i-1] + dp[i - 2]*2)%10007;
  }
  cout << dp[n] << '\n';
  return 0;



}