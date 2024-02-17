import math
def solution(storey):
    answer = 0
    

    while storey:
        cpy = storey
        c=0
        while 1:
            if cpy // (10**c) == 0:
                break
            else:
                c+=1
        if abs(cpy-10**c) >= abs(cpy-10**(c-1)):
            storey = abs(cpy-10**(c-1))
        else:
            storey = abs(cpy-10**c)
        answer+=1

    return answer

print(solution(16))