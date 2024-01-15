## 다시

import sys
input = sys.stdin.readline

n, q = map(int, input().split())

ice_graph = []

for _ in range(2**n):
    ice_graph.append(list(map(int, input().split())))

L = list(map(int, input().split()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def rotate(graph,l):
    new_graph = [[0 for _ in range(2**n)] for _ in range(2**n)]

    #i,j를 기준으로 2**l크기의 배열만 회전시킴
    for i in range(0, 2**n, 2**l):
        for j in range(0, 2 ** n, 2**l):
            for k in range(2**l):
                for m in range(2**l):
                    new_graph[i+k][j+m] = graph[i + (2**l - 1 - m)][j + k]
    return new_graph

def melt_ice(graph):
    new_graph = [[0 for _ in range(2**n)] for _ in range(2**n)]

    for x in range(2**n):
        for y in range(2**n):
            ice_count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 2**n and 0 <= ny < 2 ** n:
                    if graph[nx][ny] > 0:
                        ice_count += 1
            if ice_count < 3:
                new_graph[i][j] = graph[i][j] - 1
            else:
                new_graph[i][j] = graph[i][j]
    return new_graph

for i in range(q):
    ice_graph = rotate(ice_graph, L[i])
    ice_graph = melt_ice(ice_graph)

sum_ice = 0
check_ice = [[False for _ in range(2**n)] for _ in range(2**n)]
max_size = 0

for i in range(2 ** n):
    for j in range(2 ** n):
        if check_ice[i][j] == False and ice_graph[i][j] > 0:
            check = [[i, j]]
            sum_ice += ice_graph[i][j]
            check_ice[i][j] = True
            now_size = 1
            while check:
                x, y = check.pop(0)
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if 0 <= nx < 2**n and 0 <= ny < 2**n:
                        if ice_graph[nx][ny] > 0 and check_ice[nx][ny] == False:
                            sum_ice += ice_graph[nx][ny]
                            check.append([nx, ny])
                            check_ice[nx][ny] = True
                            now_size += 1
            max_size = max(max_size, now_size)
print(sum_ice)
print(max_size)