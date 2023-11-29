from string import ascii_uppercase
def solution(msg):
    answer = []
    lst = list(ascii_uppercase)
    dic = {}

    for i, j in enumerate(lst):
        dic[j] = i+1 


    # for i in range(len(msg)):
    #     for j in range(len(msg), i,-1):
    #         w = msg[i:j]
            
    #         if w in dic:
    #             # if (j != len(msg)):
    #             c = msg[j]
    #             w_c = w+c
    #             answer.append(dic.index(w)+1)
    #             dic.append(w_c)
    #             i = msg.index(c)


    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer


dic = list(ascii_uppercase)

# for j in (5, 0,-1):
#     print(j)
print(solution("KAKAO"))