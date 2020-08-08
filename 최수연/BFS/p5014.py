from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [-1 for _ in range(F+1)]
move = [U, -D]
#S -> G
queue = deque()
queue.append(S)
visited[S] = 0
success = 0
while queue:
    x = queue.popleft()
    if x == G:
        print(visited[x])
        success = 1
        break
    for d in move:
        nx = x + d
        if nx <= 0 or nx > F:
            continue
        if visited[nx] != -1:
            continue
        queue.append(nx)
        visited[nx] = visited[x] + 1

if success == 0:
    print("use the stairs")