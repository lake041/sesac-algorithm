from collections import deque
def dfs(v,start,map):
    v[start] = True
    print(start,end= " ")
    for i in map[start]:
        if v[i] == False:
            v[i] = True
            dfs(v,i,map)

def bfs(v,start,map):
    q = deque()
    q.append(start)

    while q:
        val = q.popleft()
        for i in map[val]:
            if v[i] == False:
                v[i] = True
                print(i, end=" ")
                q.append(i)




if __name__=="__main__":
    N, M, V = map(int, input().split())
    maps = [[] for _ in range(M + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        maps[b].append(a)
        maps[a].append(b)
    for i in maps:
        i.sort()
    visited = [False] * (N+1)
 #   print(V,end = " ")
    dfs(visited,V,maps)
    print()

    visited = [False] * (N+1)
    bfs(visited,V,maps)











