import sys
from math import floor #버림함수
input=sys.stdin.readline
x,y=map(int,input().split())
z=floor(100*y/x)
min,max=0,1000000000  #이긴 게임 수
if z>=99: print(-1)
else:
    while min<=max:
        mid=(min+max)//2
        tx=x+mid
        ty=y+mid
        if floor(100*ty/tx)>z:
            max=mid-1
        else: min=mid+1
    print(max+1)  
