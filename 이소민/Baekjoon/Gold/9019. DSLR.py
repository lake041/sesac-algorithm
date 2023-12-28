import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
def D(n):
    return (2*n) % 10000

def S(n):
    if n == 0:
        n = 9999
    else:
        n -= 1
    return n

# 0123 -> 1230
def L(n):
    if len(str(n)) == 4:
        return int(str(n)[1:]+str(n)[0])
    else:
        return n*10
    
# 0123 -> 3012
def R(n):
    if len(str(n)) == 4:
        return int(str(n)[-1]+str(n)[:-1])
    else:
        return int(str(n)[-1]+str(0)*(4-len(str(n)))+str(n)[:-1])

for i in range(n):
    a, b = map(int, input().split())
    visited = set()
    q = deque()
    q.append((a, ''))
    visited.add(a)
    while q:
        num, cmd = q.popleft()
        if num == b:
            print(cmd)
            break
        d = D(num)
        if d not in visited:
            visited.add(d)
            q.append((d, cmd+'D'))
        s = S(num)
        if s not in visited:
            visited.add(s)
            q.append((s, cmd+'S'))
        l = L(num)
        if l not in visited:
            visited.add(l)
            q.append((l, cmd+'L'))
        r = R(num)
        if r not in visited:
            visited.add(r)
            q.append((r, cmd+'R'))