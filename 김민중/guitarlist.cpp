#include <iostream>

using namespace std;


int main() {
  int V[101];
  bool dp[101][1001];

  int N,S,M;
  cin >> N >> S >> M;

  for(int i = 1; i <= N; i++) {
    cin >> V[i];
  }
  dp[0][S] = true;
  for(int i = 0; i<= N-1; i++) {
    for(int j = 0; j <= M; j++) {
      if(dp[i][j] == false) {
        continue;
      }
      if(j - V[i+1] >= 0) {
        dp[i+1][j-V[i+1]] = true;
      }
      if(j + V[i+1] <= M) {
        dp[i+1][j+V[i+1]] = true;
      }
    }
  }
  int ans = -1;
  for(int i = 0; i<= M; i++) {
    if(dp[N][i]) {
      ans = i;
    }
  }
  cout << ans << endl;

  return 0;


}