import sys
input=sys.stdin.readline
k, n = map(int, input().split())
lan = list(int(input()) for _ in range(k))
min, max = 1, max(lan)

while min <= max:
    mid = (min + max) // 2
    count = 0  # 랜선 수
    for i in lan:
        count += i // mid  # 각각의 랜선들을 몇번 자를 수 있나
    if count >= n:  # n보다 더 많이 잘리면? -> mid 길이를 늘리자 (min을 mid 위로)
        min = mid + 1
    else: # n보다 적으면? -> mid 길이 줄이자 (max를 mid 아래로)
        max = mid - 1
print(max)