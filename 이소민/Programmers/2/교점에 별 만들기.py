from itertools import combinations

def func(i, j):
    x1, y1, c1 = i 
    x2, y2, c2 = j 
    
    if x1*y2 == y1*x2: 
        return
    
    x = (y1*c2-c1*y2)/(x1*y2-y1*x2)
    y = (c1*x2-x1*c2)/(x1*y2-y1*x2)
    
    if x == int(x) and y == int(y):
        return [int(x), int(y)]

def star(points):
    x_min = points[0][0]
    y_min = points[0][1]
    x_max = points[0][0]
    y_max = points[0][1]
    for i in points:
        x_min = min(x_min, i[0])
        y_min = min(y_min, i[1])
        x_max = max(x_max, i[0])
        y_max = max(y_max, i[1])
    
    m = x_max - x_min + 1
    n = y_max - y_min + 1
    arr = [['.']*m for _ in range(n)]
    
    for x, y in points:
        arr[y-y_min][x-x_min] = '*'
    arr.reverse()
    
    return arr

def solution(line):
    answer = []
    points = []
    for i,j in combinations(line,2):
        point = func(i,j)
        if point: points.append(point)
    for i in star(points):
        answer.append(''.join(i))
    return answer