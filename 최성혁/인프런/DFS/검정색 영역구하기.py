cnt = 0

def dfs(board, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    global cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] == 1:
            board[nx][ny] = 0
            cnt += 1
            dfs(board, nx, ny)




def solution(board):
    answer = []
    global cnt

    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                cnt = 0
                dfs(board,i,j)
                answer.append(cnt)
    return answer







print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))