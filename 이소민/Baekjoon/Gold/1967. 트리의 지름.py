def dfs(start, w):
    for a,b in tree[start]:
        if visited[a] == 0:
            visited[a] = w + b
            dfs(a, w+b)

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

visited[1] = 1
dfs(1,0)
start = visited.index(max(visited))
visited = [0 for _ in range(n+1)]
visited[start] = 1
dfs(start,0)

print(max(visited))
