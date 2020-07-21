# https://www.acmicpc.net/problem/11057
# User ID : thornsal
# DP

import sys
N = int(sys.stdin.readline())          # max : 1000

my_list = [[0 for col in range(10)] for row in range(1001)]
my_list[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]        # 0 1 2 3 4 5 6 7 8 9
my_list[2] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]       # [2][0] = 1 [2][1] = 2  [2][9] = 10


for i in range(3, N+1):
    for j in range(10):
        my_list[i][j] = sum(my_list[i-1][:j+1])


print(sum(my_list[N]) % 10007)