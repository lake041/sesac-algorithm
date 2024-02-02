n,s = map(int,input().split())
arr = list(map(int,input().split()))

def dfs(level,count):
    global answer

    if count == s:
        answer += 1

    if level == n:
        return

    dfs(level + 1,count + arr[level])
    dfs(level + 1,count)


answer = 0


dfs(0,0)

# n,s = map(int,input().split())
# arr = list(map(int,input().split()))
n,s = 3,3
arr = [1,2,3]
visit = [False,False,False]
def dfs(level,count):
    global answer
    if level == n:
        if count == s:
            answer += 1
        return

    dfs(level + 1,count + arr[level])
    dfs(level + 1,count)


answer = 0
#
#
# dfs(0,0)
# if s == 0:
#     answer -= 1
#
# print('answer : ',answer)
# '''
# 5 0
# -7 -3 -2 5 8
# 3 3
# 1 2 3
# '''