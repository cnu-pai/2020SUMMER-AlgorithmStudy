# https://www.acmicpc.net/problem/11399
# User ID : thornsal
# Greedy

n = int(input())
times = list(map(int,input().split(' ')))
times.sort()

wait_time = 0
# times[0] + ( times[0] + times[1] ) +  .. + ( times[0] + times[1] + times[2] + times[3] + times[4] )

for i in range(n):
    wait_time += times[i] * (n-i)

print(wait_time)


