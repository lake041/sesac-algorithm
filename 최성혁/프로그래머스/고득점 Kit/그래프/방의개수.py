from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]


def solution(arrows):
    answer = 0
    # 사전형을 통한 노드,좌표 설정
    node, point, q = {}, {}, deque()
    point[(0, 0)] = 0
    q.append([0, 0])
    x, y = 0, 0

    for i in arrows:
        for _ in range(2):  # 모래시계형을 고려해주기 위해 point를 두 배로 늘린다
            nx = x + dx[i]  # x,y를 방향에 따라 늘려준다
            ny = y + dy[i]
            point[(nx, ny)] = 0  # 좌표값을 설정해준다
            q.append([nx, ny])
            node[(x, y, nx, ny)] = 0
            node[(nx, ny, x, y)] = 0
            x, y = nx, ny

    x, y = q.popleft()
    point[(x, y)] = 1  # 맨 처음에는 1을 넣어준다
    while q:
        nx, ny = q.popleft()

        # 이전에 방문한 적이 있는 경우
        if point[(nx, ny)] == 1:
            # 한 번도 방문한 적이 없는 노드인 경우
            if node[(x, y, nx, ny)] == 0:
                answer += 1
                node[(x, y, nx, ny)] = 1  # 노드를 방문한 것으로 바꿔준다
                node[(nx, ny, x, y)] = 1
        else:
            # 이전에 방문한 적 없는 경우
            point[(nx, ny)] = 1
            node[(x, y, nx, ny)] = 1
            node[(nx, ny, x, y)] = 1
        x, y = nx, ny

    return answer
