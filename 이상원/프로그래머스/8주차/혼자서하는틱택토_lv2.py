from collections import defaultdict
def solution(board):
    answer = 1
    dic = defaultdict(int)

    for i,j,k in board:
        dic[i] +=1
        dic[j] +=1
        dic[k] +=1
    
    numO = dic['O']
    numX = dic['X']
    # numDot = dic['.']
    if not (numO == numX or numO == numX + 1):
            return 0
    win = [0,0]
    for i,j,k in zip(board[0],board[1],board[2]):
        if i==j==k=="O":
            win[0] = 1
        if i==j==k=="X":
            win[1] = 1
    for b in board:
        if b[0]==b[1]==b[2]=="O":
            win[0] = 1
        if b[0]==b[1]==b[2]=="X":
            win[1] = 1
    if board[0][0]==board[1][1]==board[2][2]=="O":
        win[0] = 1
    if board[0][0]==board[1][1]==board[2][2]=="X":
        win[1] = 1
    if board[0][2]==board[1][1]==board[2][0]=="O":
        win[0] = 1
    if board[0][2]==board[1][1]==board[2][0]=="X":
        win[1] = 1
    if win[0] == win[1] == 1:
        return 0
    if win[0] == 1 and numO != numX + 1:
        return 0
    if win[1] == 1 and numO != numX:
        return 0
    # if cor[0]==cor[1]==0:
    #     return 1


    return 1
solution(["...", "...", "..."])
# O 갯수 < X 갯수 return 0
# O 갯수 >=  X 갯수+2 return 0
# . 갯수 == 9 return 1
# 
    # if O성공
        # return 0
    # elif X 성공
        # return 1
    # else
        # return 1
