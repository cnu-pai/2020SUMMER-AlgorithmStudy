#include <stdio.h>

int main(void) {
  int test;
  long long dp[101] = {1,1,1,1,2,2,};
  scanf("%d", &test);

  for(int i = 6; i <= 100; i++) {
    dp[i] = dp[i-1] + dp[i-5];
  }
  while(test--) {
    int n;
    scanf("%d", &n);
    printf("%lld\n", dp[n]);
  }

  return 0;
}