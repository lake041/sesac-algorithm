# 그냥
# 1번 뒤집어


def solution(sizes):
    h = [max(i) for i in sizes]
    v = [min(i) for i in sizes]
    

    return max(h) * max(v)



def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


size =[[60, 50], [30, 70], [60, 30], [80, 40]]
a = list(max(x) for x in size)
print(a)
print(solution(size))