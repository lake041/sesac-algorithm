def solution(n, words):
    answer = []
    idx = -1
    word_set = [words[0]]
    for i in range(1,len(words)):
        if words[i] in word_set:
            idx = i
            break
        if word_set[-1][-1] != words[i][0]:
            idx = i
            break
        word_set.append(words[i])
    if idx == -1:
        answer = [0,0]
    else:
        answer.append(idx%n+1)
        answer.append(idx//n+1)

    return answer