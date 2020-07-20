import sys
input = sys.stdin.readline
N = int(input())

isused_y = ['F' for _ in range(N)]
isused_diagonal1 = ['F' for _ in range(2 * N - 1)]
isused_diagonal2 = ['F' for _ in range(2 * N - 1)]

count = 0 #행에 대해서 진행

def queen(q):
    global count
    if q == N:
        count += 1
        return
    for i in range(N):
        if isused_y[i] == 'F' and isused_diagonal1[i+q] == 'F' and isused_diagonal2[q-i+N-1] == 'F':
            isused_y[i] = 'T'
            isused_diagonal1[i+q] = 'T'
            isused_diagonal2[q - i+N-1] = 'T'
            queen(q+1)
            isused_y[i] = 'F'
            isused_diagonal1[i + q] = 'F'
            isused_diagonal2[q - i + N - 1] = 'F'

queen(0)
print(count)