import sys
from collections import deque
N = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
def solution(board):
    size = 2
    num_eat = 0
    
    time = 0
    answer = 0
    q=deque()
    def findSharkAndGoal(board): # 먹을 수 있는게 있으면 가장 가까운 목표가 리턴 없으면 0리턴
        temp = []
        orgx, orgy = 0,0
        visited = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] == 9:
                    q.append([i,j,0])
                    visited[i][j] = 1
                    orgx, orgy = i,j
                if board[i][j] < size and board[i][j] != 0:
                    temp.append([i,j])
        temp.sort(key=lambda x:(abs((x[0]-orgx)-(x[1]-orgy)),x[0]))

        if temp:
            
        else:
            return 0

        # return temp[0] if temp else 0
    goal = findSharkAndGoal(board)
    


    
        # 
# q=deque()




# while q:
#     x,y,t = q.popleft()
#     for nx, ny in zip([x-1,x,x,x+1],[y,y-1,y+1,y]):
#         if 0<=nx<N and 0<=ny<N and board[nx][ny] <= size and not visited[nx][ny]: 
#             if board[nx][ny] == size or board[nx][ny] == 0: # 이동 할 수 있으면
#                 # board[x][y] = 0
#                 # board[nx][ny] = 9
#                 # q = deque()
#                 # visited = [[0]*N for _ in range(N)]
#                 visited[nx][ny] = 1
#                 q.append([nx,ny,t+1])
#                 continue
#             elif board[nx][ny] != 0 and board[nx][ny] < size: # 먹을 수 있으면
#                 # board[x][y] = 0
#                 board[nx][ny] = 9 #상어 위치 바꿔주고
#                 board[orgx][orgy] = 0
#                 q = deque()
#                 visited = [[0]*N for _ in range(N)]
#                 visited[nx][ny] =1
#                 if num_eat+1 == size:
#                     size+=1
#                     num_eat = 0
#                 else:
#                     num_eat+=1
#                 continue
#             else: # 이동 못하면
                
                
            

print(findSharkAndGoal(board))