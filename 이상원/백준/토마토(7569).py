import sys
from collections import deque
from itertools import product 
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
M, N, H = map(int, sys.stdin.readline().split()) # 가로 세로 높이
board = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]


# for b in board:
#     print(b)
# lst= ["gre", "rtn", "qefqu"]
# print(lst[:5])


# board[층][가로][세로]
q = deque()
isAll = True
for i,j,k in product(range(H), range(N), range(M)):
    if board[i][j][k] == 1:
        q.append([i,j,k,0])
    if board[i][j][k] == 0:
        isAll = False
dx = [1,-1,0,0,0,0] # z축 윗층 아래층
dy = [0,0,1,-1,0,0] # y축 위 아래
dz = [0,0,0,0,1,-1] # x축 양 옆
# print(q)
# print(isAll)
answer = 0
if not isAll:
    while q: 
        x, y, z, day = q.popleft()
        answer = max(answer, day)
        for i,j,k in zip(dx, dy,dz):
            nx, ny, nz = x+i, y+j, z+k
            if 0 <= nx and nx < H and 0 <= ny and ny < N and 0 <= nz and nz < M and board[nx][ny][nz] == 0:
                board[nx][ny][nz] = 1
                q.append([nx,ny,nz,day+1])

    for i,j,k in product(range(H),range(N), range(M)):
        if board[i][j][k] == 0:
            answer = -1
            break
    print(answer)
else:
    print(0)





