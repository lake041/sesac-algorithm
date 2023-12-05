def solution(ss):
    zeros = 0
    cnt = 0
    while 1:
        for s in ss:
            if s =="0":
                zeros+=1

        ss = ss.replace('0', '')
        c = len(ss)
        
        ss = str(format(c, 'b'))
        
        cnt+=1
        if ss == "1":
            break

    return [cnt,zeros]

print(solution("110010101001"))