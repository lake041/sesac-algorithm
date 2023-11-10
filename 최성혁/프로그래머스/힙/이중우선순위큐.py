from collections import deque


def solution(operations):
    answer = []

    queue = deque()
    for i in operations:
        li = list(i.split())
        if (li[0] == "I"):
            queue.append(int(li[1]))
        else:
            if (len(queue) != 0):
                if (int(li[1]) == 1):
                    queue.pop()
                else:
                    queue.popleft()

        queue = deque(sorted(queue))

    if (len(queue) == 0):
        answer = [0, 0]
    else:
        answer = [max(queue), min(queue)]

    return answer