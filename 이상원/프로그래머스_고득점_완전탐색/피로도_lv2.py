from itertools import combinations, permutations
def solution(k, dungeons):
    answer = -1
    cnt = len(dungeons)
    k_tmp = k
    cnt_tmp = 0
    while 1:
        per = list(permutations(dungeons, cnt))
        for p in per:
            for i in p:
                if k_tmp >= i[0]:
                    k_tmp -= i[1]
                    cnt_tmp +=1
                else:
                    cnt_tmp=0
                    break
            if cnt_tmp == cnt:
                return cnt
            else:
                k_tmp = k
                cnt_tmp = 0
        cnt -=1



# p = list(permutations([[80,20],[50,40],[30,10]],3))

# print(p)


print(solution(80,[[80,20],[50,40],[30,10]]))