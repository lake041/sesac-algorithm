# 5
# -1 2 -3 2 -1    15

# 1: 3
# 2: 4
# 3: 1
# 4: 4
# 5: 3    

# 3
# 5
# -1 2 -3 2 -1
# 1
# 0
# 4
# 1 1 1 1

def main():
    import sys
    from collections import deque
    # T = int(input())
    T = int(sys.stdin.readline())
    lst = []
    

    def sum_tal(tal):
        n = len(tal)
        answer = 0

        for i in range(n):
            q = deque()
            q.append([i,i])
            visited = [[i,i]]
            per_sum = tal[i]
            while q:
                x,y = q.popleft()
                for nx, ny in zip([x-1, x-1, x], [y, y+1, y+1]):
                    if 0<=nx<=i and i<=ny<n and [nx,ny] not in visited:
                        # temp = tal[nx:ny+1]
                        temp = tal[nx:i] + tal[i+1:ny+1] 
                        min_temp = min(temp) 
                        if min_temp >= 0:
                            per_sum = max(per_sum, sum(temp)+tal[i])
                        else:
                            per_sum = max(per_sum, sum(temp)-min_temp+tal[i]) 

                        visited.append([nx,ny])
                        q.append([nx,ny])
            answer += abs(per_sum)
            # print(i, "번 선수: ", per_sum)
        return answer%1000000007  

    for i in range(T):
        # num = int(input())
        num = int(sys.stdin.readline())
        # lst.append(list(map(int, input().split())))
        l = list(map(int, sys.stdin.readline().split()))
        # lst.append(list(map(int, sys.stdin.readline().split())))
        s = "#{0} {1}".format(i+1,sum_tal(l))
        print(s)
        # print(tal)
    # for i in range(T):
    #     # print(lst[i])
    #     s = "#{0} {1}".format(i+1,sum_tal(lst[i]))
    #     print(s)
        # print("#"+str(i+1)+" "+str(sum_tal(lst[i])))
        # print("#%d %d" %(i+1, sum_tal(lst[i])))
        


if __name__ == '__main__':
    main()

# 누적합 = [ㅁ,ㅠ,ㅊ,ㅇ,0]
# 누적합에서 최소값 = [ㅁ,ㅠ,ㅊ,ㅇ,0]
#  lst = [-1 2 -3 2 -1]

# min(lst[1:4])
# dp[1][3] = 누적합[3] - 누적합[0] - min(나빼고 민값 리스트) 

# 5
# 5
# -1 2 -3 2 -1
# 1
# 0
# 4
# 1 1 1 1
# 8
# -1 -2 -3 1 -4 1000 -5 -10
# 6
# 40 -20 -30 60 -50 -100


# 50
# 1
# 8
# -1 -2 -1 -3 -1 -5 -1 -2    

# # 40 -20 -30 60 -50 10
# 0 번 선수:  80
# 1 번 선수:  80
# 2 번 선수:  70
# 3 번 선수:  80
# 4 번 선수:  40
# 5 번 선수:  70
# #5 420

# # 40 -20 -30 60 -50 -100
# 0 번 선수:  80
# 1 번 선수:  80
# 2 번 선수:  70
# 3 번 선수:  80
# 4 번 선수:  30
# 5 번 선수:  -40
# #5 380
