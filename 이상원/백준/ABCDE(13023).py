from sys import stdin
input = stdin.readline

# 입력값 받기
n, m = map(int, input().split())
relations = [[] for _ in range(n)]
# 방문 표시
visited = [False] * 2001
# 정답 변수 생성
ans = False
# 친구 관계 입력받기
for i in range(m):
    a, b = map(int, input().split())
    # 친구 관계 등록
    relations[a].append(b)
    relations[b].append(a)

# dfs 이용
def dfs(idx, depth):
    global ans
    visited[idx] = True
    # 친구 관계가 4번 이상 연결되어 있다면
    if depth == 4:
        # 정답 표시 후 리턴
        ans = True
        return
    # 친구 관계가 존재하는지 확인
    for i in relations[idx]:
        # 아직 방문하지 않았다면
        if not visited[i]:
            # 방문 표시
            visited[i] = True
            # 재귀적으로 수행
            dfs(i, depth + 1)
            # 방문 표시 해제
            visited[i] = False

# 0번부터 N-1번까지 확인하며
for i in range(n):
    # 친구 관계 탐색
    dfs(i, 0)
    # 현재 방문 표시 해제
    visited[i] = False
    # 친구 관계가 존재한다면
    if ans:
        # 탈출
        break
# 정답이 있다면 1 출력
if ans:
    print(1)
# 정답이 없다면 0 출력
else:
    print(0)



# import sys
# from collections import deque
# N, M = list(map(int,sys.stdin.readline().split()))

# friend = [list(map(int,sys.stdin.readline().split())) for i in range(M)]
# # friend.sort()
# print(friend)

# temp_fir = friend.copy()
# visited = [0]*M
# while friend:
#     x,y = friend.pop()
#     for f in temp_fir:
#         if f == [x,y]:
#             continue





# for fri in friend:
#     q = deque()
#     q.append(fri)
#     temp = deque()
#     while q:
#         x,y = q.popleft()
#         temp.appendleft(x)
#         temp.append(y)
#         for i in fri:
#             if [x,y] == i:
#                 continue
#             if x in i:
#                 q.append([])



# while 1:
#     friend2 = friend.copy()
#     fri = []
#     while 1:
#         if not fri:
#             x,y = friend2.pop()
#             fri.append(x)
#             fri.append(y)
        
#         temp= [fri[0]]+[fri[-1]]
#         for i in range(2):
#             for j in len(friend2):
#                 if temp[i] not in friend2[j]:
#                     continue
#                 else:
#                     num = friend2[j].index(temp[i])-1
#                     if i == 0:
#                         fri = [friend2[j][num]] + fri
#                     else:
#                         fri = fri + [friend2[j][num]]
