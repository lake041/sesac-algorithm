from collections import deque

def solution(priorities, location):
    answer = 1
    queue = deque(priorities)
    # print(q)
    while len(queue) > 1:
        tmp = queue.popleft()
        if tmp < max(queue):
            queue.append(tmp)
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
        else:
            if location == 0:
                return answer
            else:
                answer += 1
                location -= 1

    return answer


print('answer : ',solution([2, 1, 3, 2],2))