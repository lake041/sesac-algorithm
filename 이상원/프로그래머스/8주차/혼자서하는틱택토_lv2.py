from collections import defaultdict
def solution(board):
    answer = -1
    dic = defaultdict(int)

    for i,j,k in board:
        dic[i] +=1
        dic[j] +=1
        dic[k] +=1
    
    numO = dic['O']
    numX = dic['X']
    numDot = dic['.']
    print(numO)
    if numO < numX or numO >= numX+2:
        return 0
    if numDot == 9:
        return 1

    cor = [0,0]

    if numO == numX and numO>=3:
        for i,j,k in zip(board[0],board[1],board[2]):
            if i==j==k=="O":
                cor[0] = 1
            if i==j==k=="X":
                cor[1] = 1
        for b in board:
            if b[0]==b[1]==b[2]=="O":
                cor[0] = 1
            if b[0]==b[1]==b[2]=="X":
                cor[1] = 1
        if board[0][0]==board[1][1]==board[2][2]=="O":
            cor[0] = 1
        if board[0][0]==board[1][1]==board[2][2]=="X":
            cor[1] = 1
        if board[0][2]==board[1][1]==board[2][0]=="O":
            cor[0] = 1
        if board[0][2]==board[1][1]==board[2][0]=="X":
            cor[0] = 1

        if cor[0] == 1:
            return 0
        if cor[1] == 1:
            return 1
        if cor[0]==cor[1]==0:
            return 1


    return 1
solution(["...", "...", "..."])
# O 갯수 < X 갯수 return 0
# O 갯수 >=  X 갯수+2 return 0
# . 갯수 == 9 return 1
# if  O 갯수 == X 갯수 
    # if O성공
        # return 0
    # elif X 성공
        # return 1
    # else
        # return 1
