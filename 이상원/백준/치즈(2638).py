import sys
from collections import deque
r,c = map(int,sys.stdin.readline().split())
bod = [list(map(int, sys.stdin.readline().split())) for i in range(r)]

# bod = [list(map(int, sys.stdin.readline().split())) for i in range(cnt)]
# for b in bod:
#     print(b)
# print()
dx =[1,-1,0,0]
dy =[0,0,1,-1]
q=deque()
def external(board,time):
    for i in range(r):
        for j in range(c):
            if board[i][j] !=1:
                board[i][j] = 2
            else:
                break
        for j in range(c-1,0,-1):
            if board[i][j] !=1:
                 board[i][j] =2
            else:
                break
    # for b in board:
    #     print(b)
    # print()
    for x in range(r):
        for y in range(c):                
            if board[x][y] == 0:
                tmp =[]
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<r and 0<=ny<c and board[nx][ny] == 2:
                        board[x][y] = 2
                        for k in range(4):
                            nx, ny = x+dx[k], y+dy[k]
                            if board[nx][ny] == 0:
                                board[nx][ny] = 2
                        break
    for x in range(r):
        for y in range(c):
            if board[x][y] == 1:
                cnt = 0
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<r and 0<=ny<c and bod[nx][ny] == 2:
                        cnt +=1
                        if cnt >=2:
                            q.append([x,y,time])
                            break  
    return board

time = 0
lst = [[2 for i in range(c)] for i in range(r)]
# print(lst)
while 1:
    bod = external(bod, time)
    while q:
        x,y,time = q.popleft()
        cnt = 0
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<r and 0<=ny<c and bod[nx][ny] == 2:
                cnt+=1
            if cnt >1:
                bod[x][y] = 0
                # for k in range(4):
                #     mx, my = x+dx[k], y+dy[k]
                #     if 0<=mx<r and 0<=my<c and bod[mx][my] == 0:
                break
    
    if bod == lst:
        break
    time+=1

print(time)
            
    # print()

# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0