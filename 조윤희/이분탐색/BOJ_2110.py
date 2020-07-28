import sys
#sys.stdin=open('input.txt',"r")
input=sys.stdin.readline
n, c = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
min,max = 1, h[-1] - h[0] #시작점과 총 거리
result = 0
while min <= max:
    mid = (min + max) // 2
    cnt = 1
    in_h = h[0]
    for i in range(1,n):
        if mid <= h[i] - in_h:
            cnt += 1
            in_h = h[i]
    if cnt >= c:
        result = mid
        min = mid + 1
    else:
        max = mid - 1
print(result)