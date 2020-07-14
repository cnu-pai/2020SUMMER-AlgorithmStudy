N = int(input())
arr = list(map(int, input().split()))
D = [-1000 for _ in range(N)]
D[0] = arr[0]
for i in range(1, N):
    D[i] = max(0, D[i-1]) + arr[i]

print(max(D))