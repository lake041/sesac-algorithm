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
        return temp[0] if temp else 0
    
    while q:
        goal = findSharkAndGoal(board)
        if goal ==0:
            print(answer)
            break
        



    
        # 
# q=deque()




while q:
    x,y,t = q.popleft()
    for nx, ny in zip([x-1,x,x,x+1],[y,y-1,y+1,y]):
        if 0<=nx<N and 0<=ny<N and board[nx][ny] <= size and not visited[nx][ny]: 
            if board[nx][ny] == size or board[nx][ny] == 0: # 이동 할 수 있으면
                # board[x][y] = 0
                # board[nx][ny] = 9
                # q = deque()
                # visited = [[0]*N for _ in range(N)]
                visited[nx][ny] = 1
                q.append([nx,ny,t+1])
                continue
            elif board[nx][ny] != 0 and board[nx][ny] < size: # 먹을 수 있으면
                # board[x][y] = 0
                board[nx][ny] = 9 #상어 위치 바꿔주고
                board[orgx][orgy] = 0
                q = deque()
                visited = [[0]*N for _ in range(N)]
                visited[nx][ny] =1
                if num_eat+1 == size:
                    size+=1
                    num_eat = 0
                else:
                    num_eat+=1
                continue
            else: # 이동 못하면
                
                
            

print(findSharkAndGoal(board))















########다른 사람 코드############


# import sys
# from collections import deque
# N = int(input())

# dx = [-1,0,0,1] # 상 좌 우 하
# dy = [0,-1,1,0]
# room = []
# sharksize = 2
# sharkeat = 0

# for i in range(N):
#     room.append([int(x) for x in sys.stdin.readline().rstrip().split()])
#     for j in range(len(room[i])):
#         if room[i][j] == 9:
#             room[i][j] = 0
#             shark_x, shark_y = i, j

# def finding_fish(sx,sy):
#     global sharksize
#     deq = deque()
#     deq.append([sx,sy])

#     visited = [[False for _ in range(N)] for _ in range(N)]
#     distance = [[0 for _ in range(N)] for _ in range(N)]
#     can_eat_fish = []

#     while deq:
#         x, y = deq.popleft()

#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if room[nx][ny] <= sharksize and not visited[nx][ny]: #이동이 가능하면
#                     visited[nx][ny] = True
#                     distance[nx][ny] = distance[x][y] + 1
#                     deq.append([nx,ny])

#                     if room[nx][ny] < sharksize and room[nx][ny] != 0: #물고기가 있고 그걸 먹을 수 있다면
#                         can_eat_fish.append([nx ,ny,distance[nx][ny]])

#     can_eat_fish.sort(key= lambda x : (x[2],x[0],x[1])) # 정렬은 거리, x, y 오름차순으로
#     return can_eat_fish

# if __name__ == '__main__':
#     ans = 0

#     while True:
#         fishlist = finding_fish(shark_x,shark_y)

#         if len(fishlist) == 0: # 먹을 수 있는 물고기가 없다면
#             print(ans)
#             exit(0)

#         shark_x, shark_y, move_time = fishlist[0]

#         sharkeat += 1
#         if sharksize == sharkeat: #먹은 물고기수와 사이즈가 같다면
#             sharkeat = 0
#             sharksize += 1

#         room[shark_x][shark_y] = 0 # 물고기 먹은 자리는 빈칸으로 바꿈
#         ans += move_time