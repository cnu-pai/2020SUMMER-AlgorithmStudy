import sys
import heapq
#sys.stdin=open('input.txt',"r")
input=sys.stdin.readline
n, k = map(int, input().split())
jewel=[]
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewel, (m, v))
bag=[]
for _ in range(k):
    c=int(input())
    bag.append(c)
bag.sort()

list=[]
res=0

for i in bag:
    while len(jewel)!=0 and i >=jewel[0][0]:
        heapq.heappush(list, -heapq.heappop(jewel)[1])
    if len(list)!=0:
        res-=heapq.heappop(list)
    elif len(jewel)==0:
        break
print(res)

