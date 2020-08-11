import sys
N = int(sys.stdin.readline())
dp = [0] * 10001

wines = [int(sys.stdin.readline()) for _ in range(N)]
wines.insert(0, 0)

dp[1] = wines[1]

if N == 1:
    print(dp[1])
elif N == 2:
    dp[2] = wines[1] + wines[2]
    print(dp[2])
else:
    dp[2] = wines[1] + wines[2]
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 1], wines[i] + dp[i - 2], wines[i] + wines[i - 1] + dp[i - 3])
    print(dp[N])

# n번째 잔까지 마셨을 때의 최대 와인양 : DP[n]
