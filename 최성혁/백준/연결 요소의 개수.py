N,M = map(int,input().split())

# 인접 리스트 초기화
graph = [[] for _ in range(N+1)]

# 정점의 개수 + 1
visited = [False] * (N+1)
# 인접 리스트와 맞추기 위해
visited[0] = True
# answer
cnt = 0
# 초기화된 인접리스트에 값 넣기
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# dfs 함수(재귀)
def dfs(v,visited):
    # 방문 리스트 방문처리
    visited[v] = True
    for i in graph[v]:
        # 방문 처리가 되어있지 않다면
        if visited[i] == False:
            # 재귀
            dfs(i,visited)



# 방문리스트 기준으로 반복문
for i in range(len(visited)):
    # 만약 방문을 안했다면
    if visited[i] == False:
        # dfs
        dfs(i,visited)
        # dfs를 마쳤다면 한 바퀴 돌고 온거
        cnt += 1
print(cnt)