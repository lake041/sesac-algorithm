def D(n):
    n *= 2
    return n%10000
def S(n):
    n -=1
    if n <0:
        n = 9999
    return n
def L(n):
    tmp = plus_zero(n)
    tmp2 = ""
    tmp2 += tmp[1:4]
    tmp2 += tmp[0]
    return int(tmp2)
def R(n):
    tmp = plus_zero(n)
    tmp2 = ""
    tmp2 += tmp[3]
    tmp2 += tmp[0:3]
    return int(tmp2)
def plus_zero(n):
    tmp =""
    if n <10:
        tmp = "000"+str(n)
    elif n < 100:
        tmp = "00"+str(n)
    elif n < 1000:
        tmp = "0"+str(n)
    else:
        tmp = str(n)
    return tmp

import sys
from collections import deque

cnt = int(sys.stdin.readline())
bod = [list(map(int, sys.stdin.readline().split())) for i in range(cnt)]

for b in bod:
    n, target = b
    visited = set()
    visited.add(n)
    answer = ""
    q = deque()
    q.append([n, ""])
    while q:
        cur, ans = q.popleft()
        
        if cur == target:
            answer = ans
            break
        D1 = D(cur)
        S1 = S(cur)
        L1 = L(cur)
        R1 = R(cur)
        if D1 not in visited:
            q.append([D1, ans+"D"])
            visited.add(D1)
        if S1 not in visited:
            q.append([S1, ans+"S"])
            visited.add(S1)
        if L1 not in visited:
            q.append([L1, ans+"L"])
            visited.add(L1)
        if R1 not in visited:    
            q.append([R1, ans+"R"])
            visited.add(R1)

    print(answer)
            


