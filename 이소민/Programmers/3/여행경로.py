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