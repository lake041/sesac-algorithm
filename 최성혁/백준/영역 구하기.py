n = int(input())
val = int(input())
computerList = [[]for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(val):
    x,y = map(int,input().split())
    computerList[y].append(x)
    computerList[x].append(y)

cnt = 0
def dfs(start):
    global cnt
    # 방문처리
    visited[start] = True
    for i in computerList[start]:
        if visited[i] == False:
            cnt += 1
            dfs(i)


dfs(1)
print(cnt)