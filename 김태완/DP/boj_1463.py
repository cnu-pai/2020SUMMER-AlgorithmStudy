# https://www.acmicpc.net/problem/1463
# User ID : thornsal
# DP

X = int(input())

counts = [X+1 for _ in range(1000001)]
counts[1] = 0
counts[2] = 1
counts[3] = 1

for i in range(1, X+1):
    if counts[i] * 3 <= X and i*3 <= X:
        counts[i*3] = min(counts[i*3], counts[i] + 1)
    if counts[i] * 2 <= X and i*2 <= X:
        counts[i*2] = min(counts[i*2], counts[i] + 1)
    if counts[i] + 1 <= X and i+1 <= X:
        counts[i+1] = min(counts[i+1], counts[i] + 1)

print(counts[X])