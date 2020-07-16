import heapq
import sys
input = sys.stdin.readline
heap = []

N = int(input())
for i in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))