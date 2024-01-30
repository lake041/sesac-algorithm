def solution(arr):
    answer = 0
    max_num = max(arr)

    temp =1
    while 1:
        tf = 1
        for a in arr:
            if (max_num*temp)%a != 0:
                temp +=1
                tf = 0
                break
        else:
            return max_num*temp




    return answer


print(solution([2,6,8,14]))
    