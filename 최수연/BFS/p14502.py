from collections import deque
import copy
N, M = map(int, input().split())
lab = list()
lab2 = [[0]*M for _ in range(N)]
virus = []
safe = 0
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#변수 입력받기
for i in range(N):
    temp = list(map(int, input().split()))
    lab.append(temp)
    for j in range(M):
        if temp[j] == 2:
            virus.append((i, j))

#안전구역 계산(BFS)
def spread():
    #큐에 바이러스 정보 삽입
    spreadTest = copy.deepcopy(lab2)
    for i in range(N):
        for j in range(M):
            if spreadTest[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if spreadTest[nx][ny] != 0:
                continue
            spreadTest[nx][ny] = 2
            queue.append((nx, ny))
    isSafe(spreadTest)

def isSafe(arr):
    check = 0
    global safe
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                check += 1
    safe = max(safe, check)

#경우의 수 계산(BackTracking)
def toWall(cnt):
    if cnt == 3:
        spread()
        return
    for i in range(N):
        for j in range(M):
            if lab2[i][j] == 0:
                lab2[i][j] = 1
                toWall(cnt + 1)
                lab2[i][j] = 0

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            lab2 = copy.deepcopy(lab)
            lab2[i][j] = 1
            toWall(1)
            lab2[i][j] = 0

print(safe)
