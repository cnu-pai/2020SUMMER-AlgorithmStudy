from collections import deque

N, K = map(int, input().split())
visited = [-1 for _ in range(100001)]
queue = deque()
queue.append(N)
visited[N] = 0
while visited[K] == -1:
    x = queue.popleft()
    for dx in -1, 1, x:
        nx = x + dx
        if nx < 0 or nx >= 100001:
            continue
        if visited[nx] != -1:
            continue
        if dx == x:
            queue.appendleft(nx)
            visited[nx] = visited[x]
        else:
            queue.append(nx)
            visited[nx] = visited[x] + 1
print(visited[K])