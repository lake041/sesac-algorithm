import math
def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        arr.append(math.ceil((100-progresses[i]) / speeds[i]))
    cnt = 0
    tmp = arr[0]
    for i in arr:
        if i > tmp:
            answer.append(cnt)
            cnt = 1
            tmp = i
        else:
            cnt += 1
    answer.append(cnt)
    return answer