from collections import deque
R, C = map(int, input().split())
queue = deque()
totalSheep = 0
totalWolf = 0
visited = [[0]*C for _ in range(R)]
fence = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if fence[i][j] == 'v':
            totalWolf += 1
        elif fence[i][j] == 'k':
            totalSheep += 1
        if fence[i][j] == 'v' and visited[i][j] == 0:
            queue.append((i, j))
            visited[i][j] = 1
            countWolf = 1
            countSheep = 0
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
                        countSheep += 1
                    elif fence[nx][ny] == 'v':
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                        countWolf += 1
            if countSheep > countWolf:
                totalWolf = totalWolf - countWolf
            else:
                totalSheep = totalSheep - countSheep

print(totalSheep, totalWolf)

