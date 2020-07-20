# https://www.acmicpc.net/problem/11727
# User ID : thornsal
# DP


# Bottom-Up

n = int(input())

my_list = [0 for _ in range(n+2)]

my_list[1] = 1
my_list[2] = 3

for i in range(3, n+1):
    my_list[i] = 2 * my_list[i-1] - 1 if i % 2 == 1 else 2 * my_list[i-1] + 1

print(my_list[n] % 10007)

# Top-Down with memo

memo = [0 for i in range(n+1)]

def dp(x):
    if x == 1:
        return 1
    elif x == 2:
        return 3
    else:
        if memo[x] != 0:
            return memo[x]
        memo[x] = dp(x-1) * 2 - 1 if x % 2 == 1 else dp(x-1) * 2 + 1
        return memo[x]

print(dp(n) % 10007)