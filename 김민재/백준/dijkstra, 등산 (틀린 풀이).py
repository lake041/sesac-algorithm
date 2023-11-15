# https://www.acmicpc.net/problem/16681

# 1 > 5 > 1 > 8이 최단거리라면
# 1을 두번째 방문할 때 기존 1보다 작아서 갱신이 안 될 수도 있다

from sys import maxsize
from collections import deque

N, M, D, E = map(int, input().split())
H = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
distance = {}
for _ in range(M):
    a, b, n = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    distance[(a, b)] = n
    distance[(b, a)] = n

memo = [-maxsize]*(N+1)

q = deque([(1, 'up', E)])
while q:
    now, status, score = q.popleft()
    for next in graph[now]:
        height_diff = H[next] - H[now]
        next_dist = distance[(now, next)]
        if status=='up' and height_diff>0: # 계속 올라감
            next_score = score + E*height_diff - D*next_dist
            if next_score > memo[next]:
                q.append((next, 'up', next_score))
                memo[next] = next_score
        elif height_diff < 0: # 피크 찍고 내려옴 or 계속 내려감
            next_score = score - D*next_dist
            if next_score > memo[next]:
                q.append((next, 'down', next_score))
                memo[next] = next_score

print(memo[-1] if memo[-1] != -maxsize else 'Impossible')

