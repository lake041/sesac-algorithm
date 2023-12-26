def solution(n):
    answer = []
    graph = []
    for i in range(1,n+1):
        graph.append([0]*i)
    
    def re(a,b,c,cnt):
        for i in range(a[0], b[0]+1):
            graph[i][a[1]] = cnt
            cnt += 1
        for i in range(b[1]+1, c[1]+1):
            graph[b[0]][i] = cnt
            cnt += 1
        j = c[1]-1
        for i in reversed(range(a[0]+1, c[0])):
            graph[i][j] = cnt
            cnt += 1
            j -= 1
        a[0] += 2
        a[1] += 1
        b[0] -= 1
        b[1] += 1
        c[0] -= 1
        c[1] -= 2
        if a[0] > b[0]:
            return graph
        re(a,b,c,cnt)
    
    re([0,0], [n-1,0], [n-1,n-1], 1)
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            answer.append(graph[i][j])
    
    return answer