def solution(rows, columns, queries):
    answer = []
    graph = [[0]*columns for _ in range(rows)]
    
    k = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = k
            k += 1
            
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        tmp = graph[x1][y1]
        m = tmp
        
        for k in range(x1+1, x2+1):
            graph[k-1][y1] = graph[k][y1]
            m = min(m, graph[k][y1])
        for k in range(y1+1, y2+1):
            graph[x2][k-1] = graph[x2][k]
            m = min(m, graph[x2][k])
        for k in reversed(range(x1, x2)):
            graph[k+1][y2] = graph[k][y2]
            m = min(m, graph[k][y2])
        for k in reversed(range(y1, y2)):
            graph[x1][k+1] = graph[x1][k]
            m = min(m, graph[x1][k])
        graph[x1][y1+1] = tmp
        answer.append(m)
          
    return answer