def isCorrect(s):
    lst = ["()", r"{}", "[]"]
    temp = s
    while 1:
        for l in lst:
            temp = "".join(temp.split(l))
        if temp == s:
            return False
        if temp == "":
            return True
        s = temp
        
    


def solution(s):
    answer = 0
    temp = ""
    leng = len(s)
    s *=2
    for i in range(leng):
        temp = s[i:i+leng]
        if isCorrect(temp):
            answer+=1

    return answer


solution("}]()[{")


print("abcdef"[2:] + "abcdef"[:2])


################다른 사람의 코드

from collections import deque
def check(s):
    while True:
        if "()" in s: s = s.replace("()","")
        elif "{}" in s: s = s.replace("{}","")
        elif "[]" in s: s = s.replace("[]","")
        else: return False if s else True       

def solution(s):
    count = 0
    queue = deque(s)

    for i in range(len(s)):
        if check(''.join(queue)): count+=1
        queue.rotate(-1)
    return count