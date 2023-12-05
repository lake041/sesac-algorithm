def solution(n, left, right):
    minus = right-left
    answer = [[max(i,j)+1 for i in range(n)] for j in range(n) if (left//n) <= j and j <= (right//n)] 
    ver = []        
    for lst in answer:
        ver += lst
    return ver[left%n:(left%n)+minus+1]

print(solution(4,	7,	14))
# for i in solution(3,2,5):
#     print(i) 
# print(solution(3,2,5))


# 4	7	14	[4,3,3,3,4,4,4,4]