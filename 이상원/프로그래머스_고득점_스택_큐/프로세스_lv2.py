from collections import deque
def solution(priorities, location):
    answer = 0
    anslist = []
    q = deque()
    for i in range (len(priorities)):
        q.append([i, priorities[i]])
    # first = q.popleft()
    while q:
      pop = q.popleft()
      a = False
      for i in range(len(q)):
        if pop[1] < q[i][1]:
            # q.append(pop)
            a = True
            break
        # else:
        #     anslist.append(pop)
      if a:
        q.append(pop)   
      else:
        anslist.append(pop)

    for i in range(len(anslist)):
        if anslist[i][0]==location:
            return i+1




lst = [1,2,34]

lst = deque(lst)
lst.extendleft([3,2,1])
# print(lst)
print(solution([1, 1, 9, 1, 1, 1], 0))
