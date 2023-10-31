from collections import deque
def solution(n, computers):
    answer = 0
    queue = deque()
    
    
    connected = [False]*n
    connected[0] = True
    queue.append(n[0])

    while queue:
        pop = queue.popleft()
        for i in range(1, len(a)):
            if connected[i] == False:
                if pop[i] == 1:
                    connected[i] = True
                    queue.append(n[i])
                

            





    return answer

connected = [False]*5
print(connected)