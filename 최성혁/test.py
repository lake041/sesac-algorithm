
import sys
T = int(sys.stdin.readline())
idx = 1
resultArr = []
for i in range(T):
    N = int(sys.stdin.readline())
    data = [sys.stdin.readline().strip() for i in range(N)]
    cnt = 0
    x,y = 0,0
    resultList = []


    for i in data:
        tmp = []
        for j in i:
            if j == ' ':
                pass
            else:
                tmp.append(j)
        resultList.append(tmp)

    for i in enumerate(resultList):
        for j in enumerate(i[1]):
            if j[1] == 'X':
                x = i[0]
                y = j[0]

    start_x = x
    start_y = y


    while 1:
        x = x - 1
        if resultList[x][y] != 'H' or x < 0:
            break
        if resultList[x][y] == 'H':
            cnt += 1
    x = start_x

    while 1:
        x = x + 1
        if resultList[x][y] != 'H' or x >= N:
            break
        if resultList[x][y] == 'H':
            cnt += 1
    x = start_x

    while 1:
        y = y -1
        if resultList[x][y] != 'H' or y < 0:
            break
        if resultList[x][y] == 'H':
            cnt += 1

    y = start_y

    while 1:
        y = y + 1
        if resultList[x][y] != 'H' or y >= N:
            break
        if resultList[x][y] == 'H':
            cnt += 1
    str_tmp = '#'+str(idx) +' '+ str(cnt)
    resultArr.append(str_tmp)
    idx += 1

for i in resultArr:
    print(i)




















