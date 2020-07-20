N, M = map(int, input().split())
arr = []

def solution(n):
    if n == M:
        for i in range(M):
            print(arr[i], end = ' ')
        print()
        return
    for i in range(N):
        arr.append(i+1)
        solution(n+1)
        arr.pop()

solution(0)