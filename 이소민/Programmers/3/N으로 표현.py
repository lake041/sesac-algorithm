def solution(N, number):
    dp = []
    for i in range(1, 9):
        case = set()
        case.add(int(str(N)*i))
        for j in range(i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    case.add(op1 - op2)
                    case.add(op1 + op2)
                    case.add(op1 * op2)
                    if op2 != 0: case.add(op1 // op2)
                    
        if number in case:
            return i
        
        dp.append(case) 
    return -1