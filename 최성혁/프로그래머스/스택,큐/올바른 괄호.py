from collections import deque


def solution(s):
    # 일단 다 넣고 후에 남아 있거나 or 남아 있지 않거나
    arr = deque(s)
    answerList = []
    while arr:
        val = arr.popleft()
        # 아무것도 없거나
        if not answerList:
            answerList.append(val)
        # '('가 마지막 원소이고 val은 ')'
        elif answerList[-1] == '(' and val == ')':
            answerList.pop()
        else:
            answerList.append(val)

    if answerList:
        return False
    else:
        return True