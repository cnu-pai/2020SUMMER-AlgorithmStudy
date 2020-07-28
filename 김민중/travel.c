#include <stdio.h>

int main(void) {
  int T,N,M;
  int a, b;
  int i;
  scanf("%d", &T);
  while(T--) {
    scanf("%d %d", &N, &M);
    for(i = 0; i < M; i++) {
      scanf("%d %d", &a, &b);
    }
    printf("%d\n", N - 1);
  }
}