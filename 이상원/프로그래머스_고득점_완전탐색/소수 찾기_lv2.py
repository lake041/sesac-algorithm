from itertools import combinations, permutations
def solution(numbers):
    answer = 0

    
    cnt =1
    while cnt <= len(numbers):
        combi = list(set(permutations(numbers, cnt)))
        for i in range(len(combi)):
            st=""
            for j in range(len(combi[i])):
                if(combi[i][0]=='0'):
                    break
                st += combi[i][j]
            if (len(st)>0):
                a = int(st)
                if is_prime_number(a):
                    answer += 1   
        cnt+=1
    
    
    
    return answer


def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    if x==1:
        return False
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


nums = "011"

print(solution(nums))