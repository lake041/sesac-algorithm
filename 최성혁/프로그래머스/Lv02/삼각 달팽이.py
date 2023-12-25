from collections import deque

def solution(n):
    dx, dy = [0, 1, -1], [1, 0, -1]
    snail, answer = [[0] * (i + 1) for i in range(n)], []
    queue = deque([(0, 0, 1, 0)])
    while queue:
        x, y, num, i = queue.popleft()
        snail[y][x] = num
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= ny < n and not snail[ny][nx]:
            queue.append((nx, ny, num + 1, i))
        else:
            i = (i + 1) % 3
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= ny < n and not snail[ny][nx]:
                queue.append((nx, ny, num + 1, i))
            else:
                break
    for floor in snail:
        answer.extend(floor)

    return answer