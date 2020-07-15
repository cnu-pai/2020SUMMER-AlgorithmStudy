import sys
#sys.stdin = open("input.txt","r")
input=sys.stdin.readline

n,pair=int(input()),int(input())
matrix=[[0]*(n+1) for _ in range(n+1)]

for i in range(pair):
    adj=list(map(int,input().split()))
    matrix[adj[0]][adj[1]]=1
    matrix[adj[1]][adj[0]]=1

def dfs(start,row,visited):
    visited+=[start]
    for search in range(len(row[start])):
        if row[start][search] and search not in visited:
            visited=dfs(search,row,visited)
    return visited
print(len(dfs(1,matrix,[]))-1)


