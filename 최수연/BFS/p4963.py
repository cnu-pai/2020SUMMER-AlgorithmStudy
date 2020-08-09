from collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    inputMap = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if inputMap[i][j] == 1 and visited[i][j] == 0:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = 1
                cnt += 1
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1):
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= h or ny < 0 or ny >= w:
                            continue
                        if visited[nx][ny] == 1 or inputMap[nx][ny] == 0:
                            continue
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
    print(cnt)