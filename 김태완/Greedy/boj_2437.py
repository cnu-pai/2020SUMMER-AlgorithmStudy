# https://www.acmicpc.net/problem/2437
# User ID : thornsal
# Greedy

n = int(input())       # 추의 개수는 1개부터 1000개까지
sum = 0
weight_list = sorted(list(map(int, input().split())))
for weight in weight_list:
    if sum + 1 < weight:
        break
    sum += weight

print(sum+1)
