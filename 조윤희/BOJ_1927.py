import sys
#sys.stdin=open('input.txt',"r")
input=sys.stdin.readline
import heapqd
n = int(input())
heap = []

#Max Heap
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
