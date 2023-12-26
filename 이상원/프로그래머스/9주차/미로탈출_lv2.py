from collections import deque
from itertools import product

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(maps):
    bod = [list(row) for row in maps]
    R, C = len(bod), len(bod[0])
    print(bod)
    lst = [[y, x] for y, x in product(range(R), range(C)) if bod[y][x] == "S"]
    print(lst)
    sy, sx = next((y, x) for y, x in product(range(R), range(C)) if bod[y][x] == "S")
    print(sy,sx)

   

solution(["OSOOL","XXSXO","OOOOO","OXXXX","OOOOE"])