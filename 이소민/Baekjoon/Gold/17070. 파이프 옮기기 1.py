def solution():
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]
	
    for r in range(1, N):
        for c in range(1, N):
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]            
            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()

# 내 풀이
# n=int(input())
# board = []
# for _ in range(n):
#     board.append(list(map(int,input().split())))

# dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
# # x,y,방향 = cnt
# if board[0][2] != 1:
#     dp[0][2][0] = 1
# if board[0][2] != 1 and board[1][1] != 1 and board[1][2] != 1:
#     dp[1][2][2] = 1

# for x in range(n):
#     for y in range(n):        
#         for d in range(3):
#             if dp[x][y][d] != 0:
#                 if d == 0 or d == 1:
#                     if d == 0 and y+1 < n and board[x][y+1] != 1:
#                         dp[x][y+1][d] += dp[x][y][d] # 가로 일 때 가로 방향으로 추가
#                     if d == 1 and x+1 < n and board[x+1][y] != 1:
#                         dp[x+1][y][d] += dp[x][y][d] # 세로 일 때 가로 방향으로 추가
#                     if x+1 < n and y+1 < n and board[x+1][y+1] != 1 and board[x+1][y] != 1 and board[x][y+1] != 1:
#                         dp[x+1][y+1][2] += dp[x][y][d] # 가로, 세로 둘 다 대각선 방향으로 추가
#                 # 대각선일 경우 세 방향 모두 추가
#                 if d == 2:
#                     if y+1 < n and board[x][y+1] != 1:
#                         dp[x][y+1][0] += dp[x][y][d]
#                     if x+1 <n and board[x+1][y] != 1:
#                         dp[x+1][y][1] += dp[x][y][d]
#                     if x+1 < n and y+1 < n and board[x+1][y+1] != 1 and board[x+1][y] != 1 and board[x][y+1] != 1:
#                         dp[x+1][y+1][2] += dp[x][y][d]

# print(sum(dp[n-1][n-1]))
