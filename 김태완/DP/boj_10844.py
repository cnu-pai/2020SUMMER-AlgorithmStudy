# https://www.acmicpc.net/problem/10844
# User ID : thornsal
# DP

import sys
N = int(sys.stdin.readline()) # max : 100

my_list = [[0 for col in range(10)] for row in range(N+1)]
my_list[1] = ([0, 1, 1, 1, 1, 1, 1, 1, 1, 1]) # 0 1 2 3 4 5 6 7 8 9

# my_list[i][j] = ( i자리 숫자이면서 j로 끝나는 수의 개수 )

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            my_list[i][j] = my_list[i-1][j+1]
        elif j == 9:
            my_list[i][j] = my_list[i-1][j-1]
        else:
            my_list[i][j] = my_list[i-1][j-1] + my_list[i-1][j+1]

print(sum(my_list[N]) % 1000000000)