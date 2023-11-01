from collections import deque

def solution(n,m,path):
    answer = 1
    q = deque()
    q.append([0,0])
    dx = [-1, 1,0,0]
    dy = [0,0,-1,1]
    
    
    while q:
        x, y = q.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
    
    
    return answer

print("wdwd")


