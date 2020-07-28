#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int main() {
  int dp[1001] = {0,};
  int N;
  cin >> N;
  dp[1] = 1;
  for(int i = 1; i<= N; i++) {
    int num;
    cin >> num;
    if(dp[i] == 0) {
      break;
    }
    for(int j = 1; j <= num; j++) {
      if(i + j > 1000) {
        break;
      }
      if(dp[i + j]>dp[i] + 1 || dp[i+j]==0) {
        dp[i+j] = dp[i]+1;
      }
    }
  }
  if(dp[N] == 0) {
    cout << -1 <<endl;
  }else {
    cout << dp[N]-1 << endl;
  }
  return 0;
}