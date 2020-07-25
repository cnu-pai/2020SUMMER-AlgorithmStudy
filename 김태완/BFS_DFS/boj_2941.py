from collections import deque

n, m, v = map(int, input().split()) # 정점 개수, 간선 개수, 시작 정점
graph = {i+1: set() for i in range(n)}



def dfs(graph, start):
    visited = []
    stack = [start]
    visited.append(start)

    while stack:
        top = stack[-1]
        unvisited = graph[top] - set(visited)
        sorted_unvisited = sorted(unvisited)
        if unvisited:
            stack.append(sorted_unvisited[0])
            visited.append(sorted_unvisited[0])
        else:
            stack.pop()
    return visited


def bfs(graph, start):

    my_queue = deque([start])
    visited = [start]

    while my_queue:
        popped = my_queue.popleft()
        for v in sorted(list(graph[popped])):
            if v not in visited:
                visited.append(v)
                my_queue.append(v)
    return visited


if __name__ == "__main__":

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    print(*dfs(graph, v))
    print(*bfs(graph, v))

