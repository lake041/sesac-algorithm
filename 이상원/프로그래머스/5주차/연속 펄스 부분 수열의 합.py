
def solution(sequence):
    answer = 0
    seq = sequence.copy()
    pur = 1
    for i in range(len(sequence)):
        sequence[i] *= pur
        pur *= -1
        seq[i] *= pur
    max_sum = 0
    tmp = 0
    for s in sequence:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)
    tmp = 0
    for s in seq:
        tmp += s
        if tmp < 0:
            tmp = 0
        max_sum = max(max_sum, tmp)
    
    answer = max_sum
    return answer


lst, ans = [2, 3, -6, 1, 3, -1, 2, 4],10
print(solution(lst))
def solution(seq):
    asp = []
    for index, num in enumerate(seq):
        if index%2 == 0:
            asp.append(asp[-1]+num if asp else num)
        else:
            asp.append(asp[-1]-num if asp else -num)
            
    ans = max(
        max(asp),
        -min(asp),
        +max(asp)-min(asp),
        -min(asp)+max(asp)
    )
        
    return ans