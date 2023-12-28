# '''
# 1) 'L'까지 최단거리
# 2) 'E'까지 최단거리
# -> visited 배열로 각 칸수 +1씩
# '''
# from collections import deque
#
#
# def bfs(maps, x, y, answer, flag, maps_visited):
#     lst = []
#     q = deque()
#     q.append([x, y])
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     while q:
#         for i in range(len(q)):
#             x, y = q.popleft()
#             print('flag : ', flag, 'x , y ', x, y)
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#
#                 if 0 <= nx < len(maps) and 0 <= ny < len(maps) and maps[nx][ny] == 'O' and flag == True:
#                     answer += 1
#                     maps[nx][ny] = 'R'
#                     q.append([nx, ny])
#                 elif 0 <= nx < len(maps) and 0 <= ny < len(maps) and maps[nx][ny] == 'L' and flag == True:
#                     lst.append([nx, ny])
#                     lst.append(answer)
#                     maps_visited[nx][ny] = answer
#                     lst.append(maps_visited)
#                     return lst
#                 elif 0 <= nx < len(maps) and 0 <= ny < len(maps) and maps[nx][ny] == 'E' and flag == False:
#                     lst.append([nx, ny])
#                     lst.append(answer)
#                     return maps_visited[nx][ny]
#                 elif 0 <= nx < len(maps) and 0 <= ny < len(maps) and maps[nx][ny] == 'O' and flag == False:
#                     maps[nx][ny] = 'R'
#                     maps_visited[nx][ny] = maps_visited[x][y] + 1
#                     q.append([nx, ny])
#
#     return lst
#
#
# def solution(maps):
#     answer = 0
#     x, y = 0, 0
#     tmp = []
#     flag = True
#     maps_visited = []
#     for i in range(len(maps)):
#         maps[i] = list(maps[i])
#         tmp = [0] * len(maps[i])
#         maps_visited.append(tmp)
#
#     for i, i_val in enumerate(maps):
#         for j, j_val in enumerate(i_val):
#             if j_val == 'S':
#                 x, y = i, j
#                 break
#
#     tmp = bfs(maps, x, y, 1, flag, maps_visited)
#     print(tmp)
#     if len(tmp) == 0:
#         return -1
#     else:
#         answer = tmp[1]
#         x, y = tmp[0][0], tmp[0][1]
#         tmp = []
#         for i, i_val in enumerate(maps):
#             for j, j_val in enumerate(i_val):
#                 if j_val == 'R':
#                     maps[i][j] = 'O'
#                 if j_val == 'S':
#                     maps[i][j] = 'O'
#         flag = False
#         tmp = bfs(maps, x, y, answer, flag, maps_visited)
#         print(tmp)
#         return tmp[1] - 1
#

from collections import deque

def bfs(start,end,maps):
    # 세로
    n = len(maps)
    # 가로
    m = len(maps[0])
    q = deque()

    # 방문 배열 초기화
    visited = [[False] * m for i in range(n)]

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    # start 위치 + cost 초기화
    for idx,i_val in enumerate(maps):
        for jdx,j_val in enumerate(i_val):
            if j_val == start:
                q.append((idx,jdx,0))

    while q:
        x,y,cost = q.popleft()
        if maps[x][y] == end:
            return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X':
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,cost + 1))
    return -1





def solution(maps):
    pathFirst = bfs('S','L',maps)
    pathSecond = bfs('L','E',maps)
    if pathFirst != -1 and pathSecond != -1:
        return pathFirst + pathSecond
    else:
        return -1




print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
