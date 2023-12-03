from collections import deque

def solution(n,vertex):
    # vertex
    queue = deque()

    # visited
    visited = [0] * (n + 1)

    # 인접리스트 생성을 위한 초기화
    graph = [[] for _ in range(len(vertex))]

    # 인접리스트 표현
    for a, b in vertex:
        graph[b].append(a)
        graph[a].append(b)

    queue.append(1)
    visited[1] = 1

    while queue:
        val = queue.popleft()
        for i in graph[val]:
            if not visited[i]:
                # 방문 노드에서 이전 노드 + 1
                visited[i] = visited[val] + 1
                queue.append(i)
    targetNum = max(visited)
    return visited.count(targetNum)



print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
