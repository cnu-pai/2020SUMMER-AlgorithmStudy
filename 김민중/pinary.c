#include <stdio.h>

int main(void) {
  
  long long int N;
  long long int dp[95][2] = {};
  scanf("%lld", &N);
  dp[1][0] = 1;
  dp[1][1] = 1;

  for(int i = 2; i<=N; i++) {
    dp[i][0] = dp[i-1][0] + dp[i-1][1];
    dp[i][1] = dp[i-1][0];
  }
  printf("%lld\n",dp[N][1]);



  return 0;
}