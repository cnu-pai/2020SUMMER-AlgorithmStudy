#include <stdio.h>

int han(int n);
int main() {
    int inputNum;
    int result;
    scanf("%d", &inputNum);
    result = han(inputNum);
    printf("%d",result);
}
int han(int n) {
    int i, count = 0;
    int three, two, one;
    
    if(n<100) {
        return n;
    }else {
        for(i=100; i<=n; i++) {
            three = i/100;
            two = (i%100)/10;
            one = (i%100)%10;
            if((three - two) == (two - one))
                count++;
        }
        return (99+count);
    }
}