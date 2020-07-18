N, M = map(int, input().split())
arr = [0 for _ in range(N+1)]
isused = ['F' for _ in range(N+1)]
def solution(n,idx):
    if n == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return
    for i in range(idx, N+1):
        if isused[i] == 'F':
            arr[n] = i
            isused[i] = 'T'
            solution(n+1, i+1)
            isused[i] = 'F'

solution(0, 1)

