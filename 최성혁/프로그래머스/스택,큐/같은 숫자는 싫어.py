from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = []
    while arr:  # 큐가 빌 때까지 반복
        current = arr.popleft()  # 현재 원소 가져오기
        if answer:
            if current != answer[-1]:
                answer.append(current)
        else:
            answer.append(current)

    return answer

print(solution([4,4,4,3,3]))
