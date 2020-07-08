# https://www.acmicpc.net/problem/11047
# User ID : thornsal
# Greedy

n, k = map(int,input().split(' '))
count = 0
coins = [int(input()) for _ in range(n)][::-1]
for coin in coins:
    count += k // coin
    k %= coin
print(count)

# previous

# n, k = map(int,input().split(' '))
#
# coins = []
# count = 0
#
# for _ in range(n):
#     coins.append(int(input()))
#
# coins.reverse()
#
# for coin in coins:
#     if k >= coin:
#         count += k//coin
#         k = k - coin * (k//coin)
#
# print(count)



