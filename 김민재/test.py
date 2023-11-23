from collections import deque

# 사전 순: Down, Left, Right, UP

D = {
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
}

def solution(R, C, sy, sx, ey, ex, k):
    bod = [[0]*R for _ in range(C)]
    sy, sx, ey, ex = map(lambda x: x-1, [sy, sx, ey, ex])
    
    ans = ''
    q = deque([(sy, sx, '')])
    while q:
        y, x, routes = q.popleft()
        if len(routes) == k:
            if (y, x) == (ey, ex):
                ans = routes
                break
            else:
                continue
        
        for direction in ('d', 'l', 'r', 'u'):
            ny, nx = y+D[direction][0], x+D[direction][1]
            if 0<=ny<R and 0<=nx<C:
                q.append((ny, nx, routes+direction))
    
    return ans if ans else "impossible"