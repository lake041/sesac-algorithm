# https://www.acmicpc.net/problem/16681

from heapq import heappush, heappop
from sys import stdin, maxsize
input = stdin.readline

N, M, D, E = map(int, input().split())
h = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, n = map(int, input().split())
    graph[a].append((b, n))
    graph[b].append((a, n))

def dijkstra(graph, start):
    memo = [maxsize]*(N+1) # start로부터의 최소 거리
    memo[start] = 0 # start부터 start까지의 거리는 0
    q = []
    heappush(q, (memo[start], start))
    
    while q:
        acc_dist, stopover = heappop(q) # 경유지와 경유지까지의 누적 거리 합
        if memo[stopover] < acc_dist: # 현재 메모된 최소 거리가 acc_dist보다 작다면 더 볼 필요 없음
            continue
        for next_dest, plus_dist in graph[stopover]: # 다음 행선지와 다음 행선지까지의 거리 
            if h[stopover] >= h[next_dest]: # 현재 경유지보다 높지 않다면 continue
                continue
            new_acc_dist = acc_dist + plus_dist # 새로운 누적 거리 합
            if new_acc_dist < memo[next_dest]: # 새로운 누적 거리 합이 기존에 메모된 거리보다 작다면
                memo[next_dest] = new_acc_dist # 메모를 업데이트하고
                heappush(q, (new_acc_dist, next_dest)) # 큐에 집어넣음
    return memo

dist1 = dijkstra(graph, 1) # 1로부터의 최소 거리
dist2 = dijkstra(graph, N) # N으로부터의 최소 거리

ans = []
for i in range(2, N):
    if dist1[i]!=maxsize and dist2[i]!=maxsize:
        ans.append(h[i]*E-(dist1[i]+dist2[i])*D) # 1-경유지-N 최소 거리 케이스
print(max(ans) if ans else "Impossible")