def solution(tar):
    answer = 0
    tar.sort(key = lambda x:[x[1],x[0]])

    ce = 0 # 현재 end
    for s,e in tar:
        if s>=ce: # 현재end 보다 새로나온 미사일 s가 크거나 같으면(개구간이라 같으면도 넣어줘야댐) 요격 필요
            answer+=1
            ce = e
        # else -> 그렇지 않은 경우는 이미 요격된 경우임
    return answer




t = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
t.sort(key = lambda x:[x[1],x[0]])

print(solution(t))



