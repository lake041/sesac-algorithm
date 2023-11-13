from itertools import permutations
def solution(numbers):
    def isPrime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False  
        return True
    arr = []
    s = set()
    for i in range(1,len(numbers)+1):
        for j in list(permutations(numbers, i)):
            arr.append(''.join(j))
    for i in arr:
        s.add(int(i))
    answer = 0
    for i in s:
        if isPrime(i) and i != 0 and i!= 1: 
            answer += 1
    return answer