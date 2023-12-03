def DFS(start, graph, visited, link_status):
    count = 1
    visited[start] = True

    for adjacent_vertex in graph[start]:
        if not visited[adjacent_vertex] and link_status[start][adjacent_vertex]:
            count += DFS(adjacent_vertex, graph, visited, link_status)

    return count

def solution(n, wires):
    answer = float("inf")

    link_status = [[True] * (n + 1) for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [False] * (n + 1)
        link_status[a][b] = False
        count_a = DFS(a, graph, visited, link_status)
        count_b = DFS(b, graph, visited, link_status)
        link_status[a][b] = True

        answer = min(answer, abs(count_a - count_b))

    return answer
