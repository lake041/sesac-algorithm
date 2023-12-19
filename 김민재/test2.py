import sys

def main():
    t = int(sys.stdin.readline())
    for tc in range(t):
        n = int(sys.stdin.readline())
        board = []
        for _ in range(n):
            board.append(list(sys.stdin.readline().split()))
        for p in range(n):
            for q in range(n):
                if (board[p][q]) == 'X':
                    x1 = p
                    y1 = q
        b1 = board[x1][:y1]
        b1 = b1[::-1]
        b2 = board[x1][y1+1:]
        b3 = []
        for i in range(x1):
            b3.append(board[i][y1])
        b3 = b3[::-1]
        b4 = []
        for i in range(x1+1, n):
            b4.append(board[i][y1])
        
        b_list = [b1, b2, b3, b4]
        count = 0
        for b in b_list:
            status = 0
            for i in b:
                if (status == 0):
                    if (i == 'Y'):
                        break
                    elif (i == 'H'):
                        status = 1
                elif (status == 1):
                    if (i == 'Y'):
                        break
                    elif (i == 'H'):
                        status = 2
            if (status == 2):
                count += 1
        print("#" + str(tc+1) + " " + str(count))

if __name__ == '__main__':
    main()


'''
3
8
L L H L L L L L
L L H L L L L L
L L Y L L L L L
H H X L L L H H
L L L L L L L L
L L Y L L L L L
L L Y L L L L L
L L L L L L L L
8
L L H L L L L L
L L H H L L L L
L L Y H L L L L
H H L L L L H H
H H L X H Y H L
L L Y H L L L L
L L Y H L L L L
L L L Y L L L L
8
L L H L L L L L
L L H H L L L L
L H Y X L Y H Y
H H L L L L H H
H L L H H Y H L
L L Y H L L L L
L L Y H L L L L
L L L Y L L L L
'''