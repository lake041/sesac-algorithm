import numpy as np

def solution(rows, columns, queries):
    matrix = [[i+(j*rows)+1 for i in range(rows)] for j in range(columns)]
    print(matrix)
    a=np.array(matrix)
    answer = []
    return matrix

for i in solution(6,	6,	[[1,1,100,97]])[2:5+1,2:4+1]:
    print(i)

def rotate1(matrix):
    temp = 0

    # while 1:
    #     if temp != 0:

    #     temp = matrix[0][1]
    #     matrix[0][1] = matrix[0][0]  

from collections import deque
def solution(height, width, queries):
    answer = []
    # [1] 행렬 초기화
    board = []
    for y in range(height):
        b = []
        for x in range(width):
            b.append((y*width) + (x+1))
        board.append(b)
    # [2] 회전
    for y1, x1, y2, x2 in queries:
        y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1
        tmp = deque()
        
        for y in range(y1,y2):
            tmp.append(board[y][x1])
        for x in range(x1,x2):
            tmp.append(board[y2][x])
        for y in range(y2,y1,-1):
            tmp.append(board[y][x2])
        for x in range(x2,x1,-1):
            tmp.append(board[y1][x])
        
        tmp.append(tmp.popleft())
        answer.append(min(tmp))
        
        for y in range(y1,y2):
            board[y][x1] = tmp.popleft()
        for x in range(x1,x2):
            board[y2][x] = tmp.popleft()
        for y in range(y2,y1,-1):
            board[y][x2] = tmp.popleft()
        for x in range(x2,x1,-1):
            board[y1][x] = tmp.popleft()
        
    return answer