import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = list()
for i in range(n):
    coin.append(int(input()))

count = [0 for _ in range(k+1)]
count[0] = 1
for i in coin:
    for j in range(i, k+1):
        count[j] += count[j-i]

print(count[k])