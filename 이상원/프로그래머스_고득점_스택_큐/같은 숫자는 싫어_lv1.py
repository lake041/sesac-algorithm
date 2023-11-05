def solution(arr):
    answer = []
    
    
    for ar in arr:
        if len(answer) >0:
            if answer[-1] != ar:
                answer.append(ar)
        else:
            answer.append(ar)
        
    
    return answer



print(solution([1,1,3,3,0,1,1]))