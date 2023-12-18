def solution(A, B):
    answer = 0
    for a in range(max(min(A), min(B))+1, 2, -1):
        bool_A = (any(num % a != 0 for num in A)) # 하나라도 a로 못나누면 false 
        if (not bool_A):
            bool_B = (any(num % a == 0 for num in B)) 
            if (not bool_B):
                answer = a
                break
        
        bool_A = (any(num % a == 0 for num in A))
        if (not bool_A):    
            bool_B = (any(num % a != 0 for num in B)) 
            if (not bool_B):
                answer = a
                break
        
    return answer


print(solution([10, 20], [5, 17]))

print(any(num % 10 != 0 for num in [10, 20])) 

# def getMyDivisor(n):
#     divisorsList = []
#     for i in range(2, int(n**(1/2)) + 1):
#         if (n % i == 0):
#             divisorsList.append(i) 
#             if ( (i**2) != n) : 
#                 divisorsList.append(n // i)
#     # divisorsList.sort()
#     return max(divisorsList)
# print(getMyDivisor(2))
# print(any([True,True,True])) # True
# print(any([False, False, False])) # False
# print(any([False, True, False])) # True
# for a in range(2, max(A[0], B[0])):
#     bool_A = (all(num % a == 0 for num in A)) # true false -> false 
#     # 모두 a으로 나눌 수 있으면 True -> 하나라도 a로 나눌 수 없으면 Fasle
#     bool_B = (any(num % a == 0 for num in A)) # true ture -> true / 
#     # 하나라도 a로 나눌 수 있으면 True -> 모두 a로 못나누면 False  
#     bool_A = (all(num % a != 0 for num in A)) 
#     # 모두 a으로 나눌 수 없으면 True -> 하나라도 a로 나눌 수 있으면 false
#     bool_B = (any(num % a != 0 for num in A)) 
#     # 하나라도 a로 나눌 수 없으면 True  -> 모두 a로 나눌수 있으면 false
