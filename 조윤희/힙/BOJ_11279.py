import sys
import heapq
input=sys.stdin.readline
n = int(input())
h = []
for i in range(n):
    x=int(input())
    if x==0:
        if not h: # 빈 배열
            print(0)
        else:
            print(-1*heapq.heappop(h)) #'-'붙인 수들이니까 다시 '-' 붙여서 출력해주기
    else:
        heapq.heappush(h, -x)
        # heapq는 최소힙만 지원하므로 '-'를 붙인 수들을 넣어줘야함






