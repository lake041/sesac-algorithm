# Start 부분 다르게해서 depth == 5인 경우 return 1
# 끝까지 못찾으면 return 0
'''
5 6
0 1
1 4
1 2
1 3
2 4
3 4
'''
N,M = map(int,input().split())
relations = [[] for _ in range(N)]
visited = [False] * N
flag = False

for i in range(M):
    a,b = map(int,input().split())
    relations[a].append(b)
    relations[b].append(a)

def dfs(idx,depth):
    global flag
    visited[idx] = True
    if depth == 4:
        visited[idx] = False
        flag = True
        return

    for i in relations[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i,depth+1)
            visited[i] = False

for i in range(N):
    dfs(i,0)
    print(visited)
    if flag:
        break


if flag:
    print(1)
else:
    print(0)