from itertools import permutations
import math
def solution(n, k):
    answer =[]
    
    lst = [i for i in range(1, n+1)]
    tmp=1
    for i in range(n):
        first = 0
        while 1:
            facto = math.factorial(n-tmp)
            if k > facto:
                k -= facto
                first+=1
            else:
                tmp+=1
                break
        answer.append(lst[first])
            



    print(answer)
    # for i in range()

    lst = [i for i in range(1, n+1) if i != first]
    perm =  list(permutations(lst, n-1))
    print(len(perm) /n)
    print(first)
    print("k=",k)
    print(perm)
    return [first] + list(perm[k-1])
                       #1  2  3  4  5   6    7
# print(solution(5,5)) #1 #1 #2 #6 #24 #120 #720
# print(list(permutations([1,2],2)))

print(solution(3,5)) # [3, 1, 2]
print(solution(5,40)) #[2, 4, 3, 5, 1]



from itertools import permutations
import math
def solution2(n, k):
    
    first = 1
    while math.factorial(n-1) < k:
        first+=1
        k -= math.factorial(n-1)
    
    # for i in range()

    lst = [i for i in range(1, n+1) if i != first]
    perm =  list(permutations(lst, n-1))
    print(len(perm) /n)
    print(first)
    print("k=",k)
    print(perm)
    return [first] + list(perm[k-1])