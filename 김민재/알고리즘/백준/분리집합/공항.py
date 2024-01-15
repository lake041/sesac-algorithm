# https://www.acmicpc.net/problem/10775

# 1. 첫번째 풀이: bisect
'''
ports = list(range(1, G+1))에 대해서 이분탐색으로 index 찾고 list.remove(index) 반복했다.
시간복잡도가 합쳐서 nlog(n)이므로 통과할 거라 생각했지만 시간 초과로 실패했다.
'''

# 2. 두번째 풀이: union-find
# PyPy3 300ms 통과, Python3 시간 초과

G = int(input())
P = int(input())

ports = list(range(G+1))
planes = [int(input()) for _ in range(P)]

def union(x, y): 
    x_root = find_root(x)
    y_root = find_root(y)

    if x_root < y_root:
        ports[y_root] = x_root
    if y_root < x_root:
        ports[x_root] = y_root

def find_root(plane):
    if ports[plane] == plane:
        return plane

    ports[plane] = find_root(ports[plane])
    return ports[plane]

ans = 0
for plane in planes:
    empty_port = find_root(plane)
    if not empty_port:
        break
    union(empty_port, empty_port-1)
    ans += 1
print(ans)