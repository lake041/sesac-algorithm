# https://www.acmicpc.net/problem/1202

from collections import deque
from heapq import heapify, heappop, heappush

N, K = map(int, input().split())
dias = deque(sorted([list(map(int, input().split())) for _ in range(N)]))
bags = sorted([int(input()) for _ in range(K)])

heapq = []

ans = 0
for bag in bags:
    while dias and dias[0][0] <= bag:
        weight, value = dias.popleft()
        heappush(heapq, -value)
    ans += -heappop(heapq) if heapq else 0
print(ans)