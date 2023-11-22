
from collections import deque
from pprint import pprint
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    q = deque()
    
    dx = [-1,1 ,0,0]
    dy = [0,0,-1,1]
    q.append([0,characterX, characterY])
    
    temp_x = []
    temp_y = []
    for i in range(len(rectangle)):
        for j in range(4):
            if j == 0 or j ==2:
                temp_x.append(rectangle[i][j])
            else:
                temp_y.append(rectangle[i][j])
    len_rec_x = max(temp_x)
    len_rec_y = max(temp_y)
    squres = [[0 for i in range(len_rec_x)]]*len_rec_y
    # for rec in rectangle:
    #     x1, y1, x2, y2 = rec
    #     for i in range(0, x2-x1)
            
    return squres

lst = solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],	1,	3,	7,	8)
# print(lst)

def xx(rectangle, characterX, characterY, itemX, itemY):
    field = [[-1] * 102 for i in range(102)]
    
    # 직사각형 그리기
    for r in rectangle:
    	# 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
            	# x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = -2
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 0

    cx2, cy2, ix2, iy2 = characterX*2, characterY*2, itemX*2,itemY*2

    q = deque()
    q.append([0,cx2,cy2])
    dx =[-1,1,0,0]
    dy =[0,0,-1,1]
    n = len(field) # x
    m = len(field[0]) # y
    
    while q:
        ans, x, y = q.popleft()
        if x == ix2 and y == iy2:
            answer = ans
            break
        
        field[x][y] = ans + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if 0<=nx< n and 0 <= ny < m and field[nx][ny] == 0:
                q.append([ans+1, nx,ny])
                

    return answer/2





lst = xx([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],	1,	3,	7,	8)
# # pprint(lst)
a = solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],	1,	3,	7,	8)
print(lst)
# print(*lst, sep='\n')

#%%

def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[-1] * 102 for i in range(102)]
    
    # 직사각형 그리기
    for r in rectangle:
    	# 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
            	# x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
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