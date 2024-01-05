def isSquare(i,j,board, n):
    r,c = len(board), len(board[0])
    if board[i][j] ==0:
        return 0
    nx,ny = i+n,j+n
    if nx<r and ny<c:
        for k in range(i,nx):
            if 0 in board[k][j:ny]:
                return -1
    else:
        return -1
    
    return (n+1)*(n+1)

def solution(board):
    answer = 1
    r,c = len(board), len(board[0])
    bigrc = r
    if r>=c:
        bigrc = c
    for i in range(r):
        for j in range(c):
            for k in range(1, r):
                tmp = isSquare(i,j,board, k)
                if tmp ==-1:
                    break
                answer = max(answer,tmp)
                

    
    return answer





def solution2(board):
    answer = 1 if 1 in board[0] or 1 in board[-1] else 0
    r,c = len(board), len(board[0])
    for i in range(1,r):
        for j in range(1,c):
            if board[i][j] ==1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) +1
                answer = max(answer, board[i][j])
    return answer**2

print(solution2(	[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))