import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
result = [0] * N
for i in range(N):
    while stack and towers[stack[-1]] < towers[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, result))))




