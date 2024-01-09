def dfs(start, v, campLst, cnt):
    v[start] = True

    if cnt == 5:
        return 1

    for target in campLst[start]:
        if not v[target]:
            v[target] = True
            if dfs(target, v, campLst, cnt + 1) == 1:
                return 1

    return 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    flag = False  # flag를 False로 초기화
    camp = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        camp[b].append(a)
        camp[a].append(b)

    for i in range(N):
        visited = [False] * N
        visited[i] = True
        if dfs(i, visited, camp, 1) == 1:
            flag = True
            break

    print(1 if flag else 0)
