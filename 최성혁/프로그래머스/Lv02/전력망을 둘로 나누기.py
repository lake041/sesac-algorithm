def dfs(start, v, wire, n):
    v[start] = True
    cnt = 1
    for w in wire[start]:
        if not v[w]:
            cnt += dfs(w, v, wire, n)
    return cnt

def solution(n, wires):
    wireNode = [[] for _ in range(n + 1)]

    for a, b in wires:
        wireNode[a].append(b)
        wireNode[b].append(a)

    answer = float('inf')

    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        visited[i] = True
        cnt = dfs(1, visited, wireNode, n)
        answer = min(answer, abs(n - 2 * cnt))

    return answer


print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
