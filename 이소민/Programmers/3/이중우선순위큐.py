from heapq import *
def solution(operations):
    q = []
    for i in operations:
        op, n = i.split()
        if op == 'I':
            heappush(q, int(n))
        elif op == 'D' and len(q) != 0:
            if n == "-1":
                heappop(q)
            else:
                q.sort()
                q.pop()
    if q:
        return [max(q), q[0]]
    else:
        return [0,0]