from string import ascii_uppercase
def solution(msg):
    answer = []
    dic = list(ascii_uppercase)



    for i in range(len(msg)):
        for j in range(len(msg), i,-1):
            w = msg[i:j]
            
            if w in dic:
                # if (j != len(msg)):
                c = msg[j]
                w_c = w+c
                answer.append(dic.index(w)+1)
                dic.append(w_c)
                i = msg.index(c)

    return answer


dic = list(ascii_uppercase)

# for j in (5, 0,-1):
#     print(j)
print(solution("KAKAO"))