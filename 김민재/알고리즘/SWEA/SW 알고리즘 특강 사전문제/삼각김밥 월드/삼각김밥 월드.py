from collections import deque

dy = [-1, -1, 0, 0, 1, 1]
dx = [-1, 0, -1, 1, 0, 1]

T = int(input())
for test_number in range(1, T+1):
    s, e = map(int, input().split())
    
    sy, sx, ey, ex = 0, 0, 0, 0
    for k in range(150):
        if (k-1)*k/2 < s <= k*(k+1)/2:
            sy, sx = k - 1, k - 1 - (k*(k+1)//2 - s)
        if (k-1)*k/2 < e < k*(k+1)/2:
            ey, ex = k - 1, k - 1 - (k*(k+1)//2 - e)

    q = deque([(sy, sx, 0)])
    visited = [[False]*150 for _ in range(150)]
    visited[sy][sx] = True

    while q:
        y, x, cnt = q.popleft()
        
        if (y, x) == (ey, ex):
            print(f'#{test_number} {cnt}')
            break

        for i in range(6):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny and 0<=nx<=ny and not visited[ny][nx]:
                q.append((ny, nx, cnt+1))
                visited[ny][nx] = True