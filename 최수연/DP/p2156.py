N = int(input())
wine = [int(input()) for _ in range(N)]
drink = [[0]*3 for _ in range(N+1)]

drink[1] = [0, wine[0], 0]

for i in range(2, N+1):
    drink[i][0] = drink[i-1][1] + wine[i-1] #연속 두번
    drink[i][1] = drink[i-1][2] + wine[i-1] #연속 첫번째
    drink[i][2] = max(drink[i-1][0], drink[i-1][1], drink[i-1][2]) #안마시는 경우

print(max(drink[N][0], drink[N][1], drink[N][2]))
