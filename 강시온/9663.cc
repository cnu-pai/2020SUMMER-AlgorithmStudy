#include<stdio.h>
#include<cstdlib>

using namespace std;

int queen[16]; //각 줄의 퀸을 저장
int N;
int cnt;

void backtrack(int x);

int main()
{
    scanf("%d", &N);
    for(int i=0; i<N; i++) //0번째 줄에 하나씩 퀸을 놓아본다
    {
        queen[0] = i;
        backtrack(0);
    }
    printf("%d\n", cnt);
}

void backtrack(int x) //파라매터는 퀸을 놓을 좌표
{
    //이자리에 퀸을 놓을 수 있는가?
    for(int i=0; i<x; i++)
    {
        if((queen[i] == queen[x]) || (abs(queen[i]-queen[x]) == abs(i-x)) ){
            return;
        }
    }
    
    if(x == N-1){
        cnt++; //퀸을 다 놓은 경우
        return;
    }
    
    for(int i=0; i<N; i++) //x+1번째 줄에 하나씩 퀸을 놓아본다
    {
        queen[x+1] = i;
        backtrack(x+1);
    }
}
