from collections import deque
def solution(maps):
    answer = []
    r,c = len(maps), len(maps[0])
    visited = [[0 for i in range(c)] for j in range(r)]
    q = deque()
    tmp = 0
    for x in range(r):
        for y in range(c):
            if maps[x][y] =="X" or visited[x][y]==1:
                continue
            q.append([x,y])
            tmp += int(maps[x][y])
            visited[x][y] = 1
            while q:
                a,b = q.popleft()
                print(maps[a][b])
                for nx,ny in zip([a+1, a-1,a,a],[b,b,b+1,b-1]):
                    if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and maps[nx][ny] != "X" :
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        tmp += int(maps[nx][ny])
            answer.append(tmp)
            tmp=0
        # print(answer)
    if answer==[]:
        return [-1]
    answer.sort()
    return answer