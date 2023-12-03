'''
 정확하게 순위를 매길 수 있는 선수의 수
'''
from collections import deque

# 그래프 연결 관계를 만들어 줄 때, 내가 이긴 선수가 이긴 선수는 나도 이기는 것을 기록해준다.
# 반대로 내가 진 선수가 진 선수는 나도 진다.
# 등수를 알 필요는 없기 때문에 위와 마찬가지로 기록된 경기 수가 n이라면 cnt +1
def solution(n, results):
    answer = 0

    # 승패리스트 만들어주기
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]

    # 주어지는 경기 결과를 패자, 승자 리스트에 추가해주기.
    for i, j in results:
        win[i].append(j)
        lose[j].append(i)

        # 모든 선수 순회
    for i in range(1, n + 1):
        visited = [0 for _ in range(n + 1)]
        # 방문기록 남겨주고
        visited[i] = 1
        # 이긴 선수 따라서 경기 매치 기록해주기
        q = deque([i])
        while q:
            player = q.popleft()
            for node in win[player]:
                if visited[node] == 0:
                    visited[node] = 1
                    q.append(node)
                    # 진 선수 따라서 경기 매치 기록해주기
        q = deque([i])
        while q:
            player = q.popleft()
            for node in lose[player]:
                if visited[node] == 0:
                    visited[node] = 1
                    q.append(node)

        if visited.count(1) == n:
            answer += 1

    return answer