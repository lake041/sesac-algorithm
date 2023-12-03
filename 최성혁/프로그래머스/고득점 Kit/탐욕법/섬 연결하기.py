def solution(n, costs):
    p = [i for i in range(n)]
    def findP(v):
        if p[v] != v:
            return findP(p[v])
        return v
    def unionP(a, b):
        a, b = findP(a), findP(b)
        if a < b:
            p[b] = a
        else:
            p[a] = b
    result = 0
    for cost in sorted(costs, key = lambda x: x[2]):
        a, b, c = cost
        if findP(a) != findP(b):
            unionP(a, b)
            result += c
    return result