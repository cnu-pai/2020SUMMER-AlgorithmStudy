# https://www.acmicpc.net/problem/9465
# User ID : thornsal
# DP

import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    my_list = [list(map(int, sys.stdin.readline().split())) for row in range(2)]
    my_list[0][1] += my_list[1][0]
    my_list[1][1] += my_list[0][0]
    for j in range(2, N):
        my_list[0][j] += max(my_list[1][j - 1], my_list[1][j - 2])
        my_list[1][j] += max(my_list[0][j - 1], my_list[0][j - 2])
    print(max(my_list[0][N - 1], my_list[1][N - 1]))

