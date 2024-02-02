# n,s = map(int,input().split())
# arr = list(map(int,input().split()))
#
# answer = 0
# def dfs(level,sum):
#     global answer
#
#     if level >= n:
#         return
#     sum += arr[level]
#
#     if sum == s:
#         answer += 1
#
#     dfs(level + 1,sum)
#     dfs(level + 1,sum - arr[level])
#
#
#
# sum = 0
# dfs(0,sum)
# print(answer)
#
#
#
#
# n,s = map(int,input().split())
# arr = list(map(int,input().split()))
#
# def dfs(level,count):
#     global answer
#
#     if level == n:
#         if count == s:
#             answer += 1
#         return
#
#     dfs(level + 1,count + arr[level])
#     dfs(level + 1,count)
#
#
# answer = 0
#
#
# dfs(0,0)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# '''
# 내가 맘에들어하는 풀이
n, s = map(int,input().split())
n_list = list(map(int,input().split()))

cnt = 0
visit = [False] * (n+1)
def dfs(num,sum):
	global cnt
	if num == n:
		return
	sum += n_list[num]
	if sum == s:
		cnt += 1

	dfs(num+1,sum) # 포함하는경우
	dfs(num+1,sum-n_list[num]) # 포함하지않는경우

dfs(0,0)
print(cnt)
# '''
#
# # 문어박사
# # def dfs(n,sum,cnt):
# #     global ans
# #
# #     if n == N:
# #         if sum == S and cnt >0:
# #             ans += 1
# #         return
# #
# #     dfs(n+1,sum+lst[n],cnt+1)
# #     dfs(n+1,sm,cnt+1)
# #
# #
# #
# # N,S = map(int,input().split())
# # lst = list(map(int,input().split()))
# # ans = 0
# # dfs(0,0,0)
# # print(ans)