from collections import deque


# 22.63 / 100.0
# def solution(s):
#     alphabet = list(s)
#     while 1:
#         cnt = 0
#         for i in range(1,len(alphabet)):
#             if alphabet[i-1] == alphabet[i]:
#                 cnt += 1
#                 alphabet[i-1] = 0
#                 alphabet[i] = 0
#         if cnt == 0:
#             break
#
#         if 0 in alphabet:
#             alphabet.remove(0)
#
#     print(alphabet)
#     if alphabet:
#         return -1
#     else:
#         return 0
#
#
#
# print(solution("baabaa"))


from collections import deque

def solution(s):
    alphabet = deque(s)
    resultList = []
    resultList.append(alphabet.popleft())
    while alphabet:
        tmp = alphabet.popleft()
        if resultList:
            if tmp == resultList[-1]:
                resultList.pop()
            else:
                resultList.append(tmp)
        else:
            resultList.append(tmp)
    if resultList:
        return 0
    else:
        return 1
print(solution("baabaa"))

