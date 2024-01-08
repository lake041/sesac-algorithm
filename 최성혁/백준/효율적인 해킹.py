from collections import defaultdict

cnt = 0
dic = defaultdict(int)
def dfs(start,v,r):
    global cnt

    for i in r[start]:
        if v[i] == False:
            v[i] = True
            cnt += 1
            dfs(i,v,r)


N,M = map(int,input().split())

relationship = [[] for _ in range(N + 1)]


# A가 B를 신뢰한다. (노드로 표현하면 B는 A의 부모이다.)
for _ in range(M):
    A, B = map(int, input().split())
    relationship[B].append(A)

visited = [False] *(N+1)
visited[0] = True
resultList = []
for i in range(1,N+1):
    cnt = 0
    dfs(i,visited,relationship)
    visited[0] = True
    visited = [False] * (N + 1)
    dic[i] = cnt

maxs = max(dic.values())
for i in dic:
    print(dic.values())