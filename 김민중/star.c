#include <stdio.h>

int main(void) {
  int total;
  int jimin, hansu;
  int cnt = 0;

  scanf("%d %d %d",&total, &jimin, &hansu);

  if(total < jimin || total < hansu) {
    cnt = -1;
  }else {
    while(jimin != hansu) {
      jimin = (jimin + 1) / 2;
      hansu = (hansu + 1) / 2;
      cnt++;
    }
  }
  printf("%d\n",cnt);
  return 0;
}