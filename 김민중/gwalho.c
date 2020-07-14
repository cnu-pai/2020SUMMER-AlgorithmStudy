#include <stdio.h>

#define MAXSIZE 50

int main() {
  int i,j,cnt,num;
  char arr[MAXSIZE];
  scanf("%d", &num);
  for(j=0; j<num; j++) {
    cnt = 0;
    scanf("%s", arr);
    for(i=0; i<MAXSIZE; i++) {
      if(arr[i] == '\0') {
        break;
      }
      if(arr[i] == '(') {
        cnt++;
      }else if(arr[i]==')' && cnt>0) {
        cnt--;
      }else if(arr[i]==')' && cnt<=0) {
        cnt--;
        break;
      }
    }
    if(cnt == 0) {
      printf("YES\n");
    }else {
      printf("NO\n");
    }
  }
}