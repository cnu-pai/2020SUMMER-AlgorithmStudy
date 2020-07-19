import sys
input=sys.stdin.readline

n=int(input())
stack=[]
result=[]
i=1
tmp=1
for _ in range(n):
    nn=int(input())
    while i<=nn:
        stack.append(i)
        result.append('+')
        i+=1

    if stack[-1]==nn:
        stack.pop()
        result.append('-')

    else:
        print('NO')
        tmp=0
        break
if tmp!=0:
    print(*result)