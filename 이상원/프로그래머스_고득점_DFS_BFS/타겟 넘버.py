def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]] # Stack
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

A = [4, 1, 2, 1]


print(solution([1, 1, 1, 1, 1], 3))


from collections import deque
def solution2(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer



print(solution2([4, 1, 2, 1], 3))


def solution3(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])
    length = len(numbers)

    while queue:
        pop, idx = queue.popleft()
        idx += 1
        if idx < length:
            queue.append([pop+numbers[idx], idx])
            queue.append([pop-numbers[idx], idx])
        else:
            if pop == target:
                answer +=1

    return answer








print(solution3([1, 1, 1, 1, 1], 3))
