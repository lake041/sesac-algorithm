def solution(s):
    arr = list(s.split(' '))
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    maxVal = max(arr)
    minVal = min(arr)
    answer = ''
    answer = str(minVal) + ' ' + str(maxVal)

    return answer




print(solution("1 2 3 4"))