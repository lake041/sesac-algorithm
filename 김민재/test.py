from itertools import product
import sys

def main():
    T = int(sys.stdin.readline())
    ans = []
    for test_number in range(1, T+1):
        N = int(sys.stdin.readline())
        bod = [list(sys.stdin.readline().rstrip().split()) for _ in range(N)]
        cannons = [(y, x) for y, x in product(range(N), repeat=2) if bod[y][x] == "X"]

        def f(arr, p):
            nonlocal cnt, N
            possible = False
            for i in range(p+1, N):
                if arr[i] == 'Y' or arr[i] == 'X':
                    break
                if not possible and arr[i] == 'H':
                    possible = True
                    continue
                if possible and arr[i] == 'H':
                    cnt += 1
                    break
            
            possible = False
            for i in range(p-1, -1, -1):
                if arr[i] == 'Y' or arr[i] == 'X':
                    break
                if not possible and arr[i] == 'H':
                    possible = True
                    continue
                if possible and arr[i] == 'H':
                    cnt += 1
                    break

        cnt = 0
        for y, x in cannons:
            row = bod[y]
            col = [row[x] for row in bod]

            f(row, x)
            f(col, y)

        TEST_NUMBER = "#" + str(test_number)
        ANSWER = cnt
        ans.append((TEST_NUMBER, ANSWER))
    
    for a, b in ans:
        print(a, b)

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