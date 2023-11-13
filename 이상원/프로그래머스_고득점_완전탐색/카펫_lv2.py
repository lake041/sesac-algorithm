def solution2(brown, yellow):
    answer = []
    anslst = []
    sums = brown+yellow

    # if yellow%2==1:
    #     return [yellow+2, 3]
    if (yellow-1)*2+8 == brown:
        return [yellow+2, 3]

    a = int(brown/2)
    for i in range(1,brown):
        for j in range(1,brown):
            if i*j == sums:
                if [i,j] not in anslst:
                    anslst.append([j,i])

    if len(anslst) == 1:
        return anslst[0]    
    
    temp = [i-j for i,j in anslst]
    i = temp.index(min(temp)) 

    return anslst[i]

def solution(brown, yellow):
    answer = []
    total = brown + yellow                  # a * b = total
    for b in range(1,total+1):
        if (total / b) % 1 == 0:            # total / b = a
            a = total / b
            if a >= b:                      # a >= b
                if 2*a + 2*b == brown + 4:  # 2*a + 2*b = brown + 4 
                    return [a,b]
            
    return answer
print(solution(10,2))

print(solution(24,24))

print(solution(8,1))
print(solution(12,4)) ## 4,4 

print(solution(14,4)) # 6,3

print(solution(14,6)) #5,4 

print(solution(18,6)) # 8,3
