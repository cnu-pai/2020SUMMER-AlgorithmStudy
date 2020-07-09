# https://www.acmicpc.net/problem/1931
# User ID : thornsal
# Greedy

count = 0
n = int(input())

conference = [tuple(map(int, input().split(' '))) for _ in range(n)]
conference.sort(key=lambda element: (element[1], element[0]))

selected = min(conference, key = lambda element : element[1])
count += 1

for c in conference[1:]:
    if selected[1] > c[0]:
        continue
    else:
        selected = c
        count += 1
print(count)








