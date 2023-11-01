from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])  # 맵 크기

    dx = [1, -1, 0, 0]  # 상하좌우
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((1, 0, 0))  # 이동 칸, row, column

    maps[0][0] = 0  # 시작 위치 방문 표시

    # BFS
    while queue:
        cnt, i, j = queue.popleft()
        for k in range(4):
            r = i + dx[k]
            c = j + dy[k]
            if r == n - 1 and c == m - 1:  # 가장 먼저 도착한 것이 가장 짧은 거리
                return cnt + 1
            if -1 < r < n and -1 < c < m and maps[r][c]:  # 맵을 넘어가지 않고 1이라면
                queue.append((cnt + 1, r, c))
                maps[r][c] = 0  # 방문할 위치를 미리 방문 표시

    return -1  # 전부 순회해도 도달하지 못함