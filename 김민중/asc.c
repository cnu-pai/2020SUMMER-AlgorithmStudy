#include <stdio.h>
#define size 10001

int cnt[size] = {0, };

int main(void) {
  int n, num;

  scanf("%d", &n);
  for (int i = 0; i<n; i++){
    scanf("%d",&num);
    cnt[num]++;
  }
  for(int i = 0; i<=size; i++) {
    if(cnt[i] == 0) {
      continue;
    }
    for(int j = 0; j<cnt[i]; j++) {
      printf("%d\n", i);
    }
  }
  return 0;
}