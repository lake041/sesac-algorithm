from collections import defaultdict, deque

def solution(arrows):
    answer = 0
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0) 

    visited = defaultdict(int) 
    visited_dir = defaultdict(int)

    q = deque([now]) 
    for i in arrows:
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            q.append(next)
            now = next

    now = q.popleft() 
    visited[now] = 1

    # 방의 개수 세기
    while q:
        next = q.popleft() 
        if visited[next] == 1: 
            if visited_dir[(now, next)] == 0:
                answer += 1 
        else: 
            visited[next] = 1
        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next
    return answer