from collections import deque
def solution(people, limit):
    # people.sort()
    q = deque(people)
    answer = 0
    while q:
        pop = q.popleft()
        if q and limit-pop < min(q):
            answer+=1
            continue
        if not q:
            answer+=1
            break
        
        for i in range(limit-pop, 0, -1):
            if i in q:
                q.remove(i)
                answer+=1
                break




    
    return answer

print(solution([70, 50, 80, 50],	100))


def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        pop = people.pop()
        if not people:
            answer+=1
            break
        for i in range(len(people)):
            rm = i-1
            if people[i] + pop > limit:
                if rm == -1:
                    answer+=1
                    break
                else:
                    people.removeAt(rm)
                    answer+=1
                    break


    



    
    return answer
print(solution([70, 50, 80, 50],	100))