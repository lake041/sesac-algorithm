def solution(arr):
    answer = -1
    temp = []
    cnt=1
    while "+" in arr:
        for i in range(cnt,len(arr),2):
            if arr[i] == "+":
                arr[i-1] = str(int(arr[i-1]) + int(arr[i+1]))
                del arr[i]
                del arr[i]
                cnt = i
                break
    
    return sol(arr)


def sol(arr):
    if len(arr) ==3:
        return int(arr[0]) - int(arr[2])
    a=int(arr[0])
    arr.pop(0)
    arr.pop(0)
    return a - sol(arr)


def solution2(arr):
    minmax = [0, 0]
    sum_value = 0
    for idx in range(len(arr)-1, -1, -1):
        if arr[idx] == '+':
            continue
        elif arr[idx] == '-':
            tempmin, tempmax = minmax
            minmax[0] = min(-(sum_value + tempmax), -sum_value+tempmin)
            # -(sum + max):-가 식전체에 붙는 경우, -sum+min:-가 이전 -값 앞까지만 붙는 경우
            minus_v = int(arr[idx+1])
            minmax[1] = max(-(sum_value+tempmin), -minus_v+(sum_value-minus_v)+tempmax)
            # -(sum + min):-가 식전체에 붙는 경우, -v+(sum-v)+max:-가 바로 뒤의 값에만 붙는 경우
            sum_value = 0
        elif int(arr[idx]) >= 0:
            sum_value += int(arr[idx])
    minmax[1] += sum_value
    return minmax[1]
    


print(solution(["1", "-", "3", "+", "5", "-", "8"]))