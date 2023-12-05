def solution(s):
    answer = [0,0]
    while s != '0b1':
        answer[0] += 1
        answer[1] += s.count('0')
        ls = []
        for i in s:
            if i == '1':
                ls.append(i)
        s = ''.join(ls)
        s = str(bin(len(s)))
    answer[1] -= answer[0] - 1
    return answer