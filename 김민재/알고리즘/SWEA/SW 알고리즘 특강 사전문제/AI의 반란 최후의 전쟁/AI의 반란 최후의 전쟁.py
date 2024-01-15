from sys import maxsize
from itertools import permutations

T = int(input())
for test_number in range(1, T+1):
    N = int(input())
    
    agents, mins = [], []
    for i in range(N):
        a, b, c = map(int, input().split())
        s0, s1, s2 = b+c, a+c, a+b
        agents.append((s0, s1, s2))
        mins.append(min(s0, s1, s2))
    stand = sum(mins)

    if N <= 2:
        print(f'#{test_number} {-1}')
        continue

    ans = maxsize
    for p in permutations(range(N), 3):
        part = stand \
            - (mins[p[0]] + mins[p[1]] + mins[p[2]])\
            + agents[p[0]][0] + agents[p[1]][1] + agents[p[2]][2]
        ans = min(ans, part)

    print(f'#{test_number} {ans}')

'''
3
3
1 1 1
1 1 1
1 1 1
1
9 9 9
4
1 1 1
2 3 2
3 3 5
4 4 6 

1
4
1 1 1
2 3 2
3 3 5
4 4 6 

1
3
9 2 1
8 1 5
7 3 1
'''