def solution(tar):
    answer = 0
    tar.sort(key = lambda x:[x[1],x[0]])

    ce = 0
    for s,e in tar:
        if s>=ce:
            answer+=1
            ce = e

    return answer




t = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
t.sort(key = lambda x:[x[1],x[0]])

print(solution(t))



