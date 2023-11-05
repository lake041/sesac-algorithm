from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    visited = [0] * len(tickets)
    tickets.sort()
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            q.append(tickets[i][1])
            answer.append('ICN')
            visited[i] = 1
            break
    while q:
        cur = q.popleft()
        answer.append(cur)
        for i in range(len(tickets)):
            if tickets[i][0] == cur and visited[i] == 0: 
                visited[i] = 1
                q.append(tickets[i][1])
                break
    return answer