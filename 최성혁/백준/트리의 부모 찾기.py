from collections import deque

def dfs(root,p,n):

    for i in n[root]:
        if p[i] == 0:
            p[i] = root
            dfs(i,p,n)




def bfs(root,p,n):
    q = deque()
    q.append(root)
    while q:
        val = q.popleft()
        for i in n[val]:
            if p[i] == 0:
                p[i] = val
                q.append(i)










if __name__=="__main__":
    N = int(input())
    nodes = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        nodes[b].append(a)
        nodes[a].append(b)
    parents = [0] * (N + 1)
    #dfs(1,parents,nodes)
    bfs(1,parents,nodes)
    #print(parents)
    for i in range(2,N+1):
        print(parents[i])

