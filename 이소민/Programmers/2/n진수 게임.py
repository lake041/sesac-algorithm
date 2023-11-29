def n_jinsu(n, num):
    al = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    if num < n:
        return al[num]
    else:
        return n_jinsu(n, num // n) + al[num % n]

def solution(n, t, m, p):
    answer = ''
    numbers = ''
    
    for num in range(t * m):
        numbers += n_jinsu(n, num)
    
    ord = p - 1
    nl = len(numbers)
    
    for i in range(nl):
        if i % m == ord:
            answer += numbers[i]
        
        if len(answer) == t:
            break
    
    return answer
