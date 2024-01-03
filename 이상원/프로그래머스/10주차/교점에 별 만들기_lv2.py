from itertools import combinations
import math
def solution(line):
    answer = []
    comb = list(combinations(line,2))
    star=[]
    for fir,sec in comb:
        a,b,e = fir
        c,d,f = sec
        if (a*d-b*c) != 0:
            x = (b*f-e*d)/(a*d-b*c) 
            y = (e*c-a*f)/(a*d-b*c)
            if x.is_integer() and y.is_integer() and [x,y] not in star:
                star.append([int(x),int(y)])

    w1, w2 = min(star, key = lambda x : x[0])[0], max(star, key = lambda x : x[0])[0] + 1
    h1, h2 = min(star, key = lambda x : x[1])[1], max(star, key = lambda x : x[1])[1] + 1
    
    answer = [['.'] * (w2 - w1) for _ in range((h2 - h1))]

    for x, y in star:
        answer[y-h1][x-w1] = '*'

    answer.reverse()
    return [''.join(a) for a in answer]


# lines = [[1, 0, -1], [1, 0, 1]]
# lines=	[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# print(solution(lines))


from itertools import combinations
import math
def solution(line):
    answer = []
    comb = list(combinations(line,2))
    # print(comb)
    star=[]
    for fir,sec in comb:
        a,b,e = fir
        c,d,f = sec
        if (a*d-b*c) != 0:
            x = (b*f-e*d)/(a*d-b*c) 
            y = (e*c-a*f)/(a*d-b*c)
            if x.is_integer() and y.is_integer() and [x,y] not in star:
                star.append([int(x),int(y)])
    # star.sort(key=lambda x:x[1], reverse=True)

    # maxx, maxy, minx,miny = -1001,-1001,1001,1001
    # for x,y in star:
    #     maxx = max(maxx, x)
    #     maxy = max(maxy, y)
    #     minx = min(minx, x)
    #     miny = min(miny, y)
    # nx,ny = maxx-minx+1,maxy-miny+1
    w1, w2 = min(star, key = lambda x : x[0])[0], max(star, key = lambda x : x[0])[0] + 1
    h1, h2 = min(star, key = lambda x : x[1])[1], max(star, key = lambda x : x[1])[1] + 1

    result = [["." for _ in range(w2 - w1)] for _ in range(h2 - h1)]
    # print(star)
    for x,y in star:
        # rr=abs(y+tempx)
        # cc=x+tempy
        rr = x-w1
        cc = y-(h2-1)
        result[abs(cc)][rr] = "*"
    for x in result:
        answer.append("".join(x))
    # print(answer)
    return answer


lines = [[1, 0, -1], [1, 0, 1]]
lines=	[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(lines))