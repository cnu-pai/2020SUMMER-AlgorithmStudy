from collections import deque
import copy

N = int(input())
area = list()
visited = [[0]*N for _ in range(N)]
visited2 = list()

for i in range(N):
    temp = list(map(int, input().split()))
    area.append(temp)

def bfs(p, q, h):
    queue = deque()
    queue.append((p, q))
    visited2[p][q] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited2[nx][ny] == 1 or area[nx][ny] <= h:
                continue
            queue.append((nx, ny))
            visited2[nx][ny] = 1

safe = list()
queue = deque
for h in range(0, 101):
    visited2 = copy.deepcopy(visited)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > h and visited2[i][j] == 0:
                bfs(i, j, h)
                cnt += 1
    safe.append(cnt)

print(max(safe))