from itertools import permutations
def solution(k, dungeons):
    arr = []
    for permutation in permutations(dungeons):
        cnt = 0
        tmp = k
        for i in permutation:
            if i[0] <= tmp:
                tmp -= i[1]
                cnt += 1
            else:
                break
        arr.append(cnt)
    return max(arr)