def solution(triangle):
    answer = 0
    table = [[0] for i in triangle]
    table[0] = triangle[0]
    
    for i in range(1,len(triangle)):
        tmp = [0]*(i+1)
        tmp[0] = table[i-1][0] + triangle[i][0]
        tmp[-1] = table[i-1][-1] + triangle[i][-1]
        for j in range(1,len(tmp)-1):
            a,b = table[i-1][j-1] + triangle[i][j], table[i-1][j] + triangle[i][j]
            tmp[j]= max(a,b)
        
        table[i] = tmp
    return max(table[len(triangle)-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
