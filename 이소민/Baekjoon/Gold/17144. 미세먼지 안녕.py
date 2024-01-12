def clock(x1,y1,x2,y2,graph):
    tmp = graph[x1][y1]
    for k in range(x1+1, x2+1):
        graph[k-1][y1] = graph[k][y1]
    for k in range(y1+1, y2+1):
        graph[x2][k-1] = graph[x2][k]
    for k in reversed(range(x1, x2)):
        graph[k+1][y2] = graph[k][y2]
    for k in reversed(range(y1, y2)):
        graph[x1][k+1] = graph[x1][k]
    graph[x1][y1+1] = tmp

    graph[x1][y1] = -1
    graph[x1][y1+1] = 0
    return graph

def declock(x1, y1, x2, y2, graph):
    tmp = graph[x1][y1]
    for k in range(y1 + 1, y2 + 1):
        graph[x1][k - 1] = graph[x1][k]
    for k in range(x1 + 1, x2 + 1):
        graph[k - 1][y2] = graph[k][y2]
    for k in reversed(range(y1, y2)):
        graph[x2][k + 1] = graph[x2][k]
    for k in reversed(range(x1, x2)):
        graph[k + 1][y1] = graph[k][y1]
    graph[x1 + 1][y1] = tmp
    
    graph[x2][y1] = -1
    graph[x2][y1+1] = 0
    return graph

r,c,t = map(int,input().split())
board = []
for i in range(r):
    board.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            ax1,ay1 = i,j

ax,ay = ax1-1,ay1

for i in range(t):
    tmp_board = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] != 0 and board[x][y] != -1:
                cnt = 0
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    if board[nx][ny] == -1:
                        continue
                    cnt += 1
                    tmp_board[nx][ny] += board[x][y]//5
                tmp_board[x][y] += board[x][y] - (board[x][y]//5 * cnt)
    board = tmp_board
    board = declock(0,ay,ax,c-1,board)
    board = clock(ax1,ay1,r-1,c-1,board)
    
answer = 0
for i in board:
    answer += sum(i)
print(answer + 2)