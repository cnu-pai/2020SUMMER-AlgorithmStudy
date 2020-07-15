import sys
input=sys.stdin.readline
n=int(input())
#삼각형 길이 조건 : 가장 긴 변 길이 <다른 두 변 합
list=[]
for i in range(n):
    list.append(int(input()))
list.sort(reverse=True) #내림차순
flag=False
for i in range(n-2):
    if list[i]<list[i+1]+list[i+2]:
        print(list[i]+list[i+1]+list[i+2])
        flag=True
        break
if flag==False:
    print(-1)
