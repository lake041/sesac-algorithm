def solution(k, d):
    return len([0 for x in range(d+1) if x%k==0 for y in range(d+1) if y%k==0 and x**2+y**2<=d**2] )

def solution(k, d):
    answer = 0
    
    for x in range(0,d+1,k) :
        max_y = int( (d**2 - x**2)**0.5 )
        answer += (max_y // k) +1
    
    return answer

print(solution(2,4))


# for i in solution(1,5):
#     print(i)    

print(solution(1,5))