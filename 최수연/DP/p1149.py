N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]
cost = [[0]*3 for _ in range(N)]
cost[0] = RGB[0]
# print(cost)
for i in range(1, N):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + RGB[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + RGB[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + RGB[i][2]

print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2]))