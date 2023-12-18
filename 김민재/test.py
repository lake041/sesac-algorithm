import sys

def main():
    T = int(sys.stdin.readline())
    ans = []
    for test_number in range(1, T+1):
        N = int(sys.stdin.readline())
        bod = [list(sys.stdin.readline().rstrip().split()) for _ in range(N)]

        cannons = []
        for y in range(N):
            for x in range(N):
                if bod[y][x] == "X":
                    cannons.append((y, x))

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