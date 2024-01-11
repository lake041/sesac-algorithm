import heapq
a = int(input())
cards = [int(input()) for _ in range(a)]
heapq.heapify(cards)
answer = 0
while cards:
    min1 = heapq.heappop(cards)
    min2 = 0
    if cards:
        min2 = heapq.heappop(cards)
    answer += min1+min2
    heapq.heappush(cards, min1+min2)
    if len(cards) == 1:
        print(answer)
        break



# (a + b) + (a + b + c) + (a+b+c+d) ...   x    min
# 10 20 30
# 10+20 + 30+30 = 90
# 10+30 + 40+20 = 100
# 20+30 + 50+10 = 110
