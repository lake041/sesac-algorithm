# sol 1 bfs
from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN",["ICN"], []))
    
    while q:
        now, path, used = q.popleft()

        if len(used) == len(tickets):
            answer.append(path)
        
        for i, ticket in enumerate(tickets):
            if ticket[0] == now and not i in used:
                q.append((ticket[1], path+[ticket[1]], used+[i]))
    answer.sort()
    return answer[0]

# sol 2 dfs
from collections import defaultdict
def solution(tickets):
    t_dict = defaultdict(list)
    
    for s, e in tickets:
        t_dict[s].append(e)

    for t_key in t_dict.keys():
        t_dict[t_key].sort(reverse = True)
    
    answer = []
    path = ["ICN"]
    
    while path:
        now = path[-1]
        
        if now not in t_dict or len(t_dict[now]) == 0:
            answer.append(path.pop())
        else:
            path.append(t_dict[now].pop())
    return answer[::-1]

print(solution([["ICN", "a"], ["a", "b"], ["c", "a"], ["a", "c"]]))