import sys
input = sys.stdin.readline

_max = 0
def dfs(x,y,cnt):
    global _max
    _max = max(_max,cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny<0 or ny >= m:
            continue
        if board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(nx,ny,cnt+1)
            visited.remove(board[nx][ny])

n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
visited = set()
answer = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited.add(board[0][0])
dfs(0,0,1)
print(_max)