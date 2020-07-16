# https://www.acmicpc.net/problem/2865
# User ID : thornsal
# Greedy

count = 0
N, M, K = map(int, input().split(' '))

ability = []
tupled = []
result = []

for _ in range(M):
    ability.append(input().split())

for i in range(M):
    for j in range(N):
        tupled.append((ability[i][2 * j], ability[i][2 * j + 1]))

sorted_list = (sorted(tupled, key= lambda element: float(element[1]), reverse= True))

for i in range(N*M):
    if i == 0:
        result.append(sorted_list[i])
        count += 1
    else:
        if sorted_list[i][0] not in [result[x][0] for x in range(len(result))]:
            result.append(sorted_list[i])
            count += 1
    if count == K:
        break
a = (sum(float(result[x][1]) for x in range(len(result))))

print(round(a, 1))







