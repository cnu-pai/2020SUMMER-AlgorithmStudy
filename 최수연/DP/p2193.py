N = int(input())
arr = [[0]*2 for _ in range(N+1)]
for i in range(1, N+1):
    if i == 1:
        arr[i][0] = 0
        arr[i][1] = 1
    else:
        arr[i][0] = arr[i-1][0] + arr[i-1][1]
        arr[i][1] = arr[i-1][0]

print(arr[N][0]+arr[N][1])