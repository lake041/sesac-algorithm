from collections import deque


def solution(n, words):
    answer = []
    cnt = 1
    for i in range(0, len(words) + 1, n):
        tmp = words[:i]
        q = deque()
        idx = 1
        for j in range(i, min(i + n, len(words))):
            if words[j] in tmp:
                answer.append(idx)
                answer.append(cnt)
                return answer
            if j >= 1 and words[j][0] != words[j - 1][-1]:
                answer.append(idx)
                answer.append(cnt)
                return answer
            idx += 1
        cnt += 1

    answer = [0, 0]

    return answer