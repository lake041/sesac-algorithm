def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[-1] * 102 for i in range(102)]
    
    # 직사각형 그리기
    for r in rectangle:
    	# 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):

                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0

                elif field[i][j] != 0:
                    field[i][j] = 1

    cx2, cy2, ix2, iy2 = characterX*2, characterY*2, itemX*2,itemY*2

    q = deque()
    q.append([cx2,cy2])
    dx =[-1,1,0,0]
    dy =[0,0,-1,1]
    visited = [[1] * 102 for i in range(102)]
    while q:
        x, y = q.popleft()
        if x == ix2 and y == iy2:
            answer = visited[x][y] // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1
                

    return answer



[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	1	3	7	8	17
[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]	9	7	6	1	11
[[1,1,5,7]]	1	1	4	7	9
[[2,1,7,5],[6,4,10,10]]	3	1	7	10	15
[[2,2,5,5],[1,3,6,4],[3,1,4,6]]	1	4	6	3	10


