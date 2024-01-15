# from collections import deque
# tar = int(input())

# cb = ""
# q = deque()
# curr = "0"
# q.append([curr,cb, 0])
# visited = [0 for i in range(10001)]
# visited[1] = 1
# while q:
#     x,c,t = q.popleft()
#     if len(x) == tar:
#         print(t)
#         exit()
#     temp = x+c
#     templen = len(temp)
#     if c:
#         if visited[templen] == 0:
#             q.append([x+c, c, t+1])
#             visited[templen] = 1
#     if visited[len(x) -1 ] == 0 and x[:-1] != "":
#         q.append([x[:-1], c,t+1])
#         visited[len(x) -1] = 1
#     if x != c:
#         if visited[len(x)*2] == 0:
#             q.append([x,x,t+1])


from collections import deque
tar = int(input())


q = deque()
q.append([1,0,0])
visited = [0 for i in range(10001)]
visited[1] = 1
while q:
    x,c,t = q.popleft()
    if x == tar:
        print(t)
        exit()
    temp = x+c
    if c:
        if not visited[temp] or visited[temp] != c:
            q.append([x+c, c, t+1])
            visited[temp] = c
    if (not visited[x-1] or visited[temp] != c) and x-1 != 0:
        q.append([x-1, c,t+1])
        visited[x-1] = c
    if x != c:
        q.append([x,x,t+1])