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


#a>=b
#2a+2b - 4 = brown
#(a-2)*(b-2) =yellow
# => ab -2a -2b + 4 = yellow
# => ab -brown = yellow
# => ab = yellow + brown
def solution(brown, yellow):
    answer = []
    ab = brown + yellow                  # a * b = ab
    for b in range(1,ab+1):
        if (ab / b) % 1 == 0:            # ab / b = a
            a = ab / b
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
