def check_winner(board, player):
    # 가로, 세로, 대각선 체크를 한 번에 수행
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # 대각선 체크
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def count_players(board):
    # 'O'와 'X'의 개수를 세는 함수
    o_count = sum(row.count('O') for row in board)
    x_count = sum(row.count('X') for row in board)
    return o_count, x_count

def solution(board):
    # 'O'와 'X'의 개수 확인
    o_count, x_count = count_players(board)

    # 'O'의 개수가 'X'의 개수와 같거나 하나 많아야 함
    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    # 'O'와 'X' 중 어느 한 쪽이 이미 승리한 경우
    if check_winner(board, 'O') and check_winner(board, 'X'):
        return 0

    # 'O'가 승리했을 때 'O'의 개수는 'X'의 개수 + 1이어야 함
    if check_winner(board, 'O') and o_count != x_count + 1:
        return 0

    # 'X'가 승리했을 때 'O'의 개수는 'X'의 개수와 같아야 함
    if check_winner(board, 'X') and o_count != x_count:
        return 0

    return 1
