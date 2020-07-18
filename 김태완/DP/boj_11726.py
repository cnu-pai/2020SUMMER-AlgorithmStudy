# https://www.acmicpc.net/problem/11726
# User ID : thornsal
# DP ( Bottom-Up)

n = int(input())
my_list = [0 for _ in range(n+2)]

my_list[1] = 1
my_list[2] = 2

for i in range(3, n+1):
    my_list[i] = my_list[i-2]+my_list[i-1]

print(my_list[n]%10007)


# Top-Down with memoization

#
# memo = [-1 for _ in range(n+2)]
#
# def dp(x):
#     if x == 1 or x == 2:
#         return x
#     if memo[x] > -1:
#         return memo[x]
#     memo[x] = dp(x-2) + dp(x-1)
#     return memo[x]
#
# print(dp(n)%10007)