from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])  # (현재까지의 합, 인덱스)를 저장하는 큐

    while queue:
        current_sum, index = queue.popleft()

        if index == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[index]
            queue.append((current_sum + number, index + 1))
            queue.append((current_sum - number, index + 1))

    return answer
