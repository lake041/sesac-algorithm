from collections import deque
def solution(people, limit):
    # people.sort()
    # q = deque(people)
    answer = 0
    while people:
        pop = people.pop()
        # pop = q.popleft()
        if people and limit-pop < min(people):
            answer+=1
            continue
        if not people:
            answer+=1
            break
        
        for i in range(limit-pop, 0, -1):
            if i in people:
                people.remove(i)
                answer+=1
                break    
    return answer

print(solution([70, 50, 80, 50],	100))


def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        pop = people.pop()
        if people and limit-pop < people[0]:
            answer+=1
            continue
        if not people:
            answer+=1
            break
        for i in range(len(people)):
            if people[i] + pop == limit:
                people.pop(i)
                answer+=1
                break
            elif people[i] + pop > limit:
                people.pop(i-1)
                answer+=1
                break

    
    return answer
print(solution([70, 50, 80, 50],100))