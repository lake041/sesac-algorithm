import sys
from collections import deque
N, M = list(map(int, sys.stdin.readline().split()))
# n줄 m칸
board = [list(input()) for _ in range(N)]

answer = 1
q = deque()
q.append([0,0,1,[board[0][0]]])
# visited = [[0 for _ in range(M)] for _ in range(N)]
# visited[0][0]=1
while q:
    x,y,ans,visit = q.popleft()
    for nx,ny in zip([x+1,x-1,x,x],[y,y,y+1,y-1]):
        if 0<=nx<N and 0<=ny<M: # and not visited[nx][ny]:
            if board[nx][ny] not in visit:
                q.append([nx,ny,ans+1,visit+[board[nx][ny]]])
                # visited[nx][ny] = 1
                answer = max(answer, ans+1)

print(answer)