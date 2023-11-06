def solution(arr):
    answer = []
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i-1])
    answer.append(arr[-1])
    return answer