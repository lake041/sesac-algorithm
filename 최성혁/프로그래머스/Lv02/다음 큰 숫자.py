def binaryCnt(target, n):
    target_cnt, n_cnt = 0, 0
    for i in target:
        if i == '1':
            target_cnt += 1
    for j in n:
        if j == '1':
            n_cnt += 1
    print(target_cnt,n_cnt)
    if target_cnt == n_cnt:
        return True
    else:
        return False


def solution(n):
    target = n + 1
    while 1:
        binary_target, binary_n = bin(target), bin(n)
        #print(binaryCnt(binary_target, binary_n))
        if binaryCnt(binary_target, binary_n):
            return target
        target += 1


print(solution(15))