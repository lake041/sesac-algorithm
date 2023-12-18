from collections import deque


def solution(n, roads, sources, destination):
    matrix = [[] for _ in range(n + 1)]

    # 매트릭스 생성
    for a, b in roads:
        matrix[a].append(b)
        matrix[b].append(a)

    # 처음은 경로 없음으로 세팅, destination은 다른 값으로 세팅
    road_map = [-1] * (n + 1)
    road_map[destination] = float('inf')  # 여기를 수정

    queue = deque([(destination, float('inf'))])  # 여기도 수정

    while queue:
        q = queue.popleft()
        for i in matrix[q[0]]:
            if road_map[i] == -1:
                queue.append((i, q[1] - 1))
                road_map[i] = q[1] - 1

    return [road_map[j] for j in sources]

