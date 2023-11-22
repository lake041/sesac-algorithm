from collections import deque 
def solution(m, n, puddles):
    answer = 0
    q = deque()
    q.append([0,0])
    visited = [[0 for i in range(m)] for j in range(n)]
    for i,j in puddles:
        visited[j-1][i-1] = 1
    # visited[0][0] = 1
    # visited[0][1] =2
    cnt = 0
    print(visited)
    while q:
        x,y = q.popleft()
        if x == n-1 and y== m-1:
            cnt +=1
            continue
        visited[x][y] = 1
        if y<m-1:
            if visited[x][y+1] == 0: # 오른쪽이동 
                q.append([x, y+1])
        if x<n-1:
            if visited[x+1][y] == 0: # 아래쪽이동
                q.append([x+1, y])
    
    return cnt%1000000007


# q = deque([0,0])
# print(solution(4,3,[[2,2], [1,2], [3,2]]))
m = 5
n = 4
puddles = [[2, 2], [3, 2], [4, 3]]
print(solution(m,n,puddles))
# q = deque()
# q.append([0,0])
# visited = [[0 for i in range(4)] for j in range(3)]
# print(q.popleft())


from collections import deque 

def solution2(m, n, puddles):

    MOD =  1000000007

    maps = [[0] * m for _ in range(n)]
    maps[0][0] = 1
    
    for x in range(n):
        for y in range(m):
            if ([y+1,x+1] in puddles) or ((x,y) == (0,0)): 
                continue # 다음 루프 !
            maps[x][y] = (maps[x-1][y] + maps[x][y-1]) % MOD
            
    return maps[-1][-1]

# 테스트 케이스
# print(solution2(4, 3, [[2, 2]]))  # 정답: 4
print(solution2(5, 4, [[2, 2], [3, 2], [4, 3]]))


def solution3(m, n, puddles):
    answer = 0
    
    puddles = [[j, i] for [i, j] in puddles]
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):  
            if i==1 and j==1: continue 
            if [i, j] in puddles: dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    return dp[n][m]