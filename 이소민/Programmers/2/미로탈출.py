from collections import deque

def solution(maps):
    graph = [[0]* len(maps[0]) for _ in range(len(maps))]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    q = deque()
    
    def bfs(q, graph):
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] != "X" and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
        return graph
    
    
    # S -> L
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                q.append((i,j))
                graph[i][j] = 1
                graph = bfs(q, graph)
    
    x, y = -1,-1
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "L" and graph[i][j] != 0:
                answer = graph[i][j] -1
                x = i
                y = j
    # L -> E
    graph = [[0]* len(maps[0]) for _ in range(len(maps))]
    
    if x != -1 and y != -1:
        q.append((x,y))
        graph[x][y] = 1
        graph = bfs(q, graph)
    else:
        return -1
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "E" and graph[i][j] == 0:
                return -1
            if maps[i][j] == "E":
                answer += graph[i][j] -1
    
    return answer