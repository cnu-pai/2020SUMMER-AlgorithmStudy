
#sys.stdin=open('input.txt',"r")
input=sys.stdin.readline
n,m,v=map(int,input().split())

matrix=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    adj=list(map(int,input().split()))
    matrix[adj[0]][adj[1]]=1
    matrix[adj[1]][adj[0]]=1

def dfs(point,row, visited):
    visited+=[point]
    for search in range(len(row[point])):
        if row[point][search] and search not in visited:

  return visited

def bfs(point,row,visited):
    queue=[point]
    visited=[point]
    while queue:
        point=queue.pop(0)











