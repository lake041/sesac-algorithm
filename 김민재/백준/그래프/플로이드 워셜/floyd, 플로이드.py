# https://www.acmicpc.net/problem/11404

from sys import maxsize
from itertools import product

N = int(input())
M = int(input())
graph = [[maxsize]*N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for i in range(N):
    graph[i][i] = 0

for k, i, j in product(range(N), range(N), range(N)):
    if graph[i][k] + graph[k][j] < graph[i][j]:
        graph[i][j] = graph[i][k] + graph[k][j]

for i, j in product(range(N), range(N)):
    if graph[i][j] == maxsize:
        graph[i][j] = 0

for row in graph:
    print(*row)