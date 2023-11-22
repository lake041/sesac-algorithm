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


     
    


print(solution(["1", "-", "3", "+", "5", "-", "8"]))