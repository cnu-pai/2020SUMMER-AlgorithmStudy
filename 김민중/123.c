#include <stdio.h>

int main(void) {
  int dp[11];
  int T;
  scanf("%d", &T);

  
  int n;
  dp[0] = 1;
  dp[1] = 2;
  dp[2] = 4;

  for(int i = 0; i < T; i++) {
    scanf("%d", &n);
    for(int j = 3; j < n; j++) {
      dp[j] = dp[j-3] + dp[j-2] + dp[j-1];
    }
  printf("%d\n", dp[n-1]);  
  }
  




  return 0;
}