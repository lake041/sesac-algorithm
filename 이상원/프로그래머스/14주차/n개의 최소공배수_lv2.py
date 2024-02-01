def solution(arr):
    answer = 0
    max_num = max(arr)
    temp =1
    while 1:
        for a in arr:
            if (max_num*temp)%a != 0:
                temp +=1
                tf = 0
                break
        else:
            return max_num*temp
    return answer

# 가장 큰수에 temp를 곱해서 arr에 있는 원소로 다 나누어 지면 (else 문 - break 문에 걸리지 않고 끝까지 실행 된 거임)
# 가장 큰수 * temp 반환

print(solution([2,6,8,14])) # 168
    