from collections import deque
R, C = map(int, input().split())
queue = deque()
sheep = 0
wolf = 0
visited = [[0]*C for _ in range(R)]
fence = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if fence[i][j] == 'v':
            wolf += 1
        elif fence[i][j] == 'k':
            sheep += 1
        if fence[i][j] == 'v' and visited[i][j] == 0:
            queue.append((i, j))
            visited[i][j] = 1
            wolf_num = 1
            sheep_num = 0
            while queue:
                x, y = queue.popleft()
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nx, ny = dx + x, dy + y
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        continue
                    if fence[nx][ny] == '#' or visited[nx][ny] == 1:
                        continue
                    elif fence[nx][ny] == '.':
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                    elif fence[nx][ny] == 'k':
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                        sheep_num += 1
                    elif fence[nx][ny] == 'v':
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                        wolf_num += 1
            if sheep_num > wolf_num:
                wolf = wolf - wolf_num
            else:
                sheep = sheep - sheep_num








print(sheep, wolf)

