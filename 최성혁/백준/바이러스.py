from collections import deque

comN = int(input())
netWork = int(input())

computer = [[] for _ in range(comN + 1)]

# DFS
# cnt = 0
# def dfs(v,start,c):
#     global cnt
#     v[start] = True
#     for i in c[start]:
#         if v[i] == False:
#             cnt += 1
#             dfs(v,i,c)

def bfs(v,start,c):
    q = deque()
    q.append(start)
    v[start] = True
    cnt = 0

    while q:
        target = q.popleft()
        for i in c[target]:
            if v[i] == False:
                v[i] = True
                q.append(i)
        cnt += 1
    return cnt



for _ in range(netWork):
    a,b = map(int,input().split())
    computer[b].append(a)
    computer[a].append(b)


visited = [False] * (comN+1)
visited[0] = True

# dfs(visited,1,computer)
# print(cnt)

print(bfs(visited,1,computer)-1)