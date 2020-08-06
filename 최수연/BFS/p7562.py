from collections import deque
import sys
input = sys.stdin.readline
test = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for i in range(test):
    I = int(input())
    knight_x, knight_y = map(int, input().split())
    des_x, des_y = map(int, input().split())
    visited = [[-1]*I for _ in range(I)]

    queue = deque()
    queue.append((knight_x, knight_y))
    visited[knight_x][knight_y] += 1
    while queue:
        x, y = queue.popleft()
        if x == des_x and y == des_y:
            break
        for j in range(8):
            nx, ny = x + dx[j], y + dy[j]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if visited[nx][ny] != -1:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
    print(visited[des_x][des_y])



