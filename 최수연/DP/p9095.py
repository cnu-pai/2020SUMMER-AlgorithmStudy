import sys
input = sys.stdin.readline
T = int(input())
num = []
init = [1,2,4]
for i in range(T):

for i in range(T):
    n = int(input())
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for j in range(4, n+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[n])

