import time
# start = time.time()  # 시작 시간 저장
# import sys
# from collections import deque
# N, M = map(int,sys.stdin.readline().split())

# q = deque()

# time2 = 100000
# num = 0
# find = 0
# v = [N]
# q.append([N, 0])
# while q:
#     c, t = q.popleft()
#     if t>time2:
#         break
#     cp, cm, ct = c +1, c-1, c*2
#     if cp == M:
#         num+=1
#         time2 = t+1
#         find=1
#     if cm == M:
#         num+=1
#         time2 = t+1
#         find=1
#     if ct == M:
#         num+=1
#         time2 = t
#         find=1
#     if not find:
#         if cp not in v and 0<=cp<=100000 and c<M:
#             q.append([cp,t+1])
#             v.append(cp)
#         if cm not in v and 0<=cm<=100000:
#             q.append([cm,t+1])
#             v.append(cm)
#         if ct not in v and 0<=ct<=100000 and c<M:
#             if ct < 2*M:
#                 q.append([ct,t+1])
#                 v.append(ct)

# print(time2)
# print(num)
# print("time :", time.time() - start)



start = time.time()  # 시작 시간 저장
import sys
from collections import deque
N, K= map(int, sys.stdin.readline().split())
queue = deque()
queue.append(N)
way = [0]*100001 # 최대 크기
cnt, result,find = 0,0,0
while queue:
    a =  queue.popleft()
    temp = way[a]
    if a == K: # 둘이 만났을 때
        result = temp # 결과
        cnt += 1 # 방문 횟수 +1
        find = 1
        continue
    if not find:
        for i in [a-1, a+1, a*2]:
            if 0 <= i < 100001 and (way[i] == 0 or way[i]== way[a] +1): #범위 안에있고 방문하지 않았거나, 다음 방문이 이전 방문+1이면
                way[i] = way[a] + 1
                queue.append(i) 
print(result)
print(cnt)
print("time :", time.time() - start)
