def solution(msg):
    answer = []
    dictionary = {chr(i + 65): i + 1 for i in range(26)}
    next_index = 27  # 다음에 추가될 심볼의 인덱스

    i = 0
    while i < len(msg):
        w = msg[i]
        while i + 1 < len(msg) and w + msg[i + 1] in dictionary:
            i += 1
            w += msg[i]

        answer.append(dictionary[w])
        if i + 1 < len(msg):
            dictionary[w + msg[i + 1]] = next_index
            next_index += 1

        i += 1

    return answer


