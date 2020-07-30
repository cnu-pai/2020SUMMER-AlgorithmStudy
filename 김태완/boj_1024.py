N, L = map(int, input().split())

x = -1
k = 0

for i in range(L, 101):
    t = (i-1)*i // 2
    if (N - t) % i == 0 and (N - t) // i >= 0:
        x = (N - t) // i
        k = i
        break
if x == -1:
    print(-1)
else:
    for i in range(k):
        print(int(x + i))