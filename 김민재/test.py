from copy import deepcopy
from collections import deque

def solution(coin, cards):
    N = len(cards)
    takes = cards[:N//3]
    cards = cards[N//3:]
    cards = deque(cards)

    q = deque()
    q.append((takes, 0, coin))
    ans = 0
    cnt = 0
    while q:
        now, round, co = q.popleft()
        ans = max(ans, round)
        if round*2 >= len(cards):
            break
        next1, next2 = cards[round*2], cards[round*2+1]
        cases = []
        if co >= 2:
            new = deepcopy(now)
            new.append(next1)
            new.append(next2)
            cases.append((now+[next1, next2], round, co-2))
        if co >= 1:
            new = deepcopy(now)
            new.append(next1)
            cases.append((new, round, co-1))
            new = deepcopy(now)
            new.append(next2)
            cases.append((new, round, co-1))
        if co >= 0:
            new = deepcopy(now)
            cases.append((new, round, co))

        unique_list = []
        [unique_list.append(x) for x in cases if x not in unique_list]
        unique2 = []
        for case in unique_list:
            card_set, round_num, coin_num = case
            for i in range(1, N//2+2):
                if i in card_set and (N+1-i) in card_set:
                    temp_set = deepcopy(card_set)
                    temp_set.remove(i)
                    temp_set.remove(N+1-i)
                    if (temp_set, round_num+1, coin_num) not in unique2:
                        q.append((temp_set, round_num+1, coin_num))
                        unique2.append((temp_set, round_num+1, coin_num))

        cnt += 1
        # if cnt == 2:
        #     return list(q)

    return ans+1