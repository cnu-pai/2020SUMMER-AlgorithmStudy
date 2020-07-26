import sys
input = sys.stdin.readline
N = int(input())
stair_number =[[0]*10 for _ in range(N)]
result = 0


def isStairNum():
    global stair_number, N
    for i in range(1, 10):
        stair_number[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                stair_number[i][j] = stair_number[i-1][j+1]
            elif j == 9:
                stair_number[i][j] = stair_number[i-1][j-1]
            else:
                stair_number[i][j] = stair_number[i-1][j-1]+stair_number[i-1][j+1]

isStairNum()
for i in range(10):
    result += stair_number[N-1][i]
print(result%1000000000)