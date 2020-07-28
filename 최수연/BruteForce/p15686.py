import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
city = []
house = []
chicken = []

for i in range(N):
    temp = list(map(int, input().split()))
    city.append(temp)
    for j in range(N):
        if temp[j] == 1:
            house.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))

brute = list(combinations(chicken, M))

def minDist(brute, house):
    sum = 0
    for hx, hy in house:
        dist = sys.maxsize
        for cx, cy in brute:
            temp = abs(cx-hx) + abs(cy-hy)
            dist = min(dist, temp)
        sum += dist
    return sum

result = sys.maxsize
for i in range(len(brute)):
    result = min(result, minDist(brute[i], house))
print(result)
