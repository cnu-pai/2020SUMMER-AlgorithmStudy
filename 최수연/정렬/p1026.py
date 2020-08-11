N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
B = list(reversed(sorted(B)))
result = 0
for i in range(N):
    result += A[i] * B[i]

print(result)