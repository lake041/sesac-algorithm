from collections import deque

def bfs(maps, q):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y = q.popleft()
        maps[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                maps[nx][ny] = '.'
    return maps

First = []
boom = []
Third = []
Fifth = []

R, C, N = map(int, input().split())

fq = deque()
tq = deque()

# First List
for i in range(R):
    lst = list(map(str, input()))
    First.append(lst)

# boom List
for i in range(R):
    lst = ['O'] * C
    boom.append(lst)

# First List boom Check
for i in range(R):
    for j in range(C):
        if First[i][j] == 'O':
            fq.append([i, j])

# Third List
Third = bfs(boom, fq)

# Third List boom Check
for i in range(R):
    for j in range(C):
        if Third[i][j] == 'O':
            tq.append([i, j])

newboom = []

# boom List
for i in range(R):
    lst = ['O'] * C
    newboom.append(lst)

Fifth = bfs(newboom, tq)

realNewboom = []

# realNewboom List
for i in range(R):
    lst = ['O'] * C
    realNewboom.append(lst)

if N % 2 == 0:
    for row in realNewboom:
        print("".join(row))
elif N % 5 == 0:
    for row in Fifth:
        print("".join(row))
elif N % 3 == 0:
    for row in Third:
        print("".join(row))
else:
    for row in First:
        print("".join(row))
