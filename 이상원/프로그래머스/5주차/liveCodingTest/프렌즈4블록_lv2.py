def solution(m, n, board):
    answer = 0
    temp = [["1" for i in range(n)] for j in range(m)]
    board = [[j for j in i] for i in board]
    while 1:
        is_b = True
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == "#":
                    continue
                if board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                    temp[i][j] = "0"
                    temp[i+1][j] = "0"
                    temp[i][j+1]= "0"
                    temp[i+1][j+1]= "0"
                    is_b = False
        if is_b:
            break
        for i in range(1, m):
            for j in range(0, n):
                if temp[i][j] == "0" and temp[i-1][j] == "1":
                    temp[i][j] = "1"
                    pre = list(board[i-1])
                    cur = list(board[i])
                    cur[j] = pre[j]
                    pre[j] = "#"
                    board[i] = ''.join(cur)
                    board[i-1] = ''.join(pre)
        
    for i in board:
        answer += i.count('#')
    return board   


def solution2(m, n, board):
    answer = 0
    temp = [["1" for i in range(n)] for j in range(m)]
    while 1:
        is_b = True
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == "#":
                    continue
                if board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                    temp[i][j] = "0"
                    temp[i+1][j] = "0"
                    temp[i][j+1] = "0"
                    temp[i+1][j+1] = "0"
                    is_b = False
        if is_b:
            break
        for i in range(1, m):
            for j in range(0, n):
                if temp[i][j] == "0" and temp[i-1][j] == "1":
                    temp[i][j] = "1"
                    pre = list(board[i-1])
                    cur = list(board[i])
                    cur[j] = pre[j]
                    pre[j] = "#"
                    board[i] = ''.join(cur)
                    board[i-1] = ''.join(pre)
        
    for i in board:
        answer += i.count('#')
    return answer

# temp = [["1" for i in range(5)] for j in range(4)]
# temp[1][0] =2
# print(temp)

a =["CCBDE", 
    "AAADE", 
    "AAABF", 
    "CCBBF"]

# print(solution(4,5,a))

# ['###DE', 
#  '###DE', 
#  'CCBBF', 
#  'CCBBF']

# a = [[j for j in i] for i in a]
# print(a)
for row in solution(4,5,a):
    print(row)
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
