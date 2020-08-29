import sys
input = sys.stdin.readline
N, M = map(int, input().split())
first = set()
second = set()

for i in range(N):
    first.add(input().strip())
for i in range(M):
    second.add(input().strip())
inCommon = list(first&second)
print(len(inCommon))
inCommon = sorted(inCommon)
for i in inCommon:
    print(i)