from collections import deque

def bfs(target,visited):
    # 최단거리 탐색을 위한 queue 초기화
    q = deque()
    # 놀이터 지점
    q.append(0)
    # 놀이터 지점 방문
    visited[0] = True
    # ** 얼만큼 갔는지 중요한 level 초기화
    level = 0
    while q:
        # 각 노드가 level에 몇개있는지 세는 그 만큼 반복문 돌아야함
        length = len(q)
        for i in range(length):
            # 현재 방문한 노드
            tmp = q.popleft()
            #print(tmp)
            if tmp == target:
                return level
            # 방문한 노드에서 가지치기
            for val in [tmp - 1,tmp + 1 ,tmp + 5]:
                # 큐에 들어갈 값들은 주어진 범위내 + 방문하지 않은 곳
                if 0 <= val < 100000 and visited[val] == False:
                    q.append(val)
                    visited[val] = True
        # 가장 중요한 현재 어느 레벨까지 즉, 놀이터와 얼마나 멀어졌는지 거리를 측정하는 변수 한칸증가
        level += 1










for i in range(5):
    # 해당 위치를 방문했는지 체크하는 방문배열 초기화(수직선의 좌표만큼)
    visited = [False] * 10000
    # 입력받을 현수의 집의 위치
    home = int(input())
    print(bfs(home,visited))


