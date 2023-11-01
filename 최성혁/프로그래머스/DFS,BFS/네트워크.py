def solution(n, computers):
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if not visited[i] and computers[v][i]:  # computers 안의 배열 check
                dfs(i)

    answer = 0
    visited = [False] * (n)

    for node_idx in range(n):
        if not visited[node_idx]:
            dfs(node_idx)
            answer += 1  # dfs 끝날때 cnt ++
    #
    return answer
