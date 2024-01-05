def isPalin(s):
    l = len(s)
    for i in range(l//2):
        if s[i]!=s[(i+1)*-1]:
            return False
    return True
def solution(s):
    answer=len(s)
    if isPalin(s):
        return answer
    start = 0
    end = len(s)-1
    while 1:
        while end!=len(s)+1:
            if isPalin(s[start:end]):
                return end-start
            else:
                start+=1
                end+=1
        end = end-start-1
        start=0

    return answer

print(solution("abacde"))
# print(isPalin("abcdcba"))
# print("ababfbh"[0:7])
# print("qfw"[-3])