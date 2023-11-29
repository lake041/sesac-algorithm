from collections import defaultdict, deque

def solution(arrows):
    answer = 0
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0) # 현재 노드

    visited = defaultdict(int) # 노드 방문 체크
    visited_dir = defaultdict(int) # 노드 방문 경로 체크, (A,B)는 A -> B 경로를 의미

    q = deque([now]) # 방문을 위한 큐
    for i in arrows:
        # 모래 시계 형태를 막기 위해 해당 방향으로 2칸씩 추가
        for _ in range(2):
            next = (now[0] + move[i][0], now[1] + move[i][1])
            q.append(next)
            now = next

    now = q.popleft() # 현재 노드
    visited[now] = 1 # 시작 노드는 방문 처리

    # 방의 개수 세기
    while q:
        next = q.popleft() # 다음 노드

        if visited[next] == 1: # 이미 방문한 노드일 경우
            if visited_dir[(now, next)] == 0: # 해당 경로로 처음 들어온 경우
                answer += 1 # 방이 생성되므로 answer에 +1
        else: # 방문한 노드가 아닐 경우 방문 처리
            visited[next] = 1

        # 해당 노드로 들어온 경로를 방문 처리
        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next

    return answer