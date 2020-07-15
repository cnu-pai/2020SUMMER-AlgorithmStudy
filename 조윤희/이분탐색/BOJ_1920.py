import sys
#sys.stdin=open('input.txt',"r")
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

def search(a,b):
    s=0
    e=len(a)-1
    while s<=e:
        m=(s+e)//2
        if b==a[m]:
            return 1
        elif b>a[m]:
            s=m+1
        else:
            e=m-1
    return 0
a.sort() #오름차순 정렬 후 이진탐색!!

for x in range(m):
    print(search(a,b[x])) 
