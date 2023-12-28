from collections import deque
import copy
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    q = deque()
    tmp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append((i,j))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx,ny))
    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)

def wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(count+1)
                graph[i][j] = 0

answer = 0
wall(0)
print(answer)