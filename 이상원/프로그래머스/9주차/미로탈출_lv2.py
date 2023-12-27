from collections import deque
def solution(maps):
    answer = -1
    isLever = False
    R, C = len(maps), len(maps[0])
    visited = [[0 for i in range(C)] for j in range(R)]

    q = deque()
    for i in range(len(maps)):
        for j in range (len(maps[i])):
            if maps[i][j] == "X":
                visited[i][j] = -1
            if maps[i][j] == "S":
                q.append([i,j])

    dx = [1,-1,0,0] # 위 아래
    dy = [0,0,1,-1] # 양 옆
    lst = []
    cnt =0
    while q:
        x,y = q.popleft()
        tempval =visited[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx and nx < len(maps) and 0 <= ny and ny < len(maps[0]):
                if visited[nx][ny] == 0:
                    visited[nx][ny] = tempval+1
                    cnt+=1
                    visited[x][y] = -1
                    lst.append([x,y])
                    if maps[nx][ny] =="L" and isLever == False:
                        isLever=True
                        q = deque()
                        q.append([nx,ny])
                        for i in range(len(maps)):
                            for j in range (len(maps[i])):
                                if maps[i][j] == "O" or maps[i][j] == "S" or maps[i][j] == "E" :
                                    visited[i][j] = 0
                        break
                    if isLever == True and maps[nx][ny] =="E":
                        return visited[nx][ny]
                    q.append([nx,ny])   
    return answer


print(solution(["EOOOO","XXXXO","OOSOO","OXXXX","OOOOL"]))