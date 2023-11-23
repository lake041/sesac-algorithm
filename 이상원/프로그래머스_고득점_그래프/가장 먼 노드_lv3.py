from collections import deque, Counter

def solution(n, edge):
    answer = 0
    graph =[[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    
    
    for node in edge: # 각 인덱스가 노드 번호고 그 번호와 연결된 노드번호를 그래프에 넣음
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])  
    
    
    q = deque([1])
    visited[1]=0
    
    # BFS 수행
    while q :
        pop = q.popleft() 
        for i in graph[pop]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[pop] + 1
    for d in visited:
        if d == max(visited):
            answer += 1
    return answer
    # dic = Counter(visited).most_common(1)
    # print(dic.most_common())
    # if dic[0][0] != 0 or dic[0][0] != 1:
    #     return dic.most_common(1)[0][1]
    # else:
    #     return 0
    # Counter 배워서 써먹어 보려했는데 왜 안되는지 모르겠음 다시시도해보기
    
print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))