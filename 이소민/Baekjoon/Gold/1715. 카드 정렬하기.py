from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
card = [int(input()) for _ in range(n)]
heapify(card)

c = 0
s = 0

while len(card) > 1:
    n1 = heappop(card)
    n2 = heappop(card)
    c = n1 + n2
    s += c
    heappush(card, c)

print(s)
