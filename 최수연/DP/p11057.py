N = int(input())
ascendingNum = [[0]*10 for _ in range(N)]

for i in range(N):
    for j in range(10):
        if i == 0:
            ascendingNum[i][j] = j+1
        else:
            if j == 0:
                ascendingNum[i][j] = 1
            else:
                ascendingNum[i][j] = ascendingNum[i-1][j] + ascendingNum[i][j-1]


#10007로 나누기
print(ascendingNum[N-1][9] % 10007)
