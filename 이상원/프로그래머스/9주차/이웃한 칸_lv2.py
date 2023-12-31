def solution(bod, x, y):
    answer = 0
    r,c = len(bod), len(bod[0])
    for nx,ny in zip([x-1, x+1, x, x], [y,y,y+1,y-1]):
        if 0<=nx<r and 0<=ny<c:
            if bod[nx][ny] == bod[x][y]:
                answer += 1
    return answer
