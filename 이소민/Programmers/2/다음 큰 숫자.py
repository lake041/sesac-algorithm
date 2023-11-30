def solution(n):
    n_cnt = bin(n).count('1')
    tmp = n
    while True:
        tmp += 1
        tmp_cnt = bin(tmp).count('1')
        if n_cnt == tmp_cnt:
            return tmp