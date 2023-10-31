def solution(numbers, target):
    def dfs(i, sum):
        nonlocal cnt
        if i == len(numbers):
            if sum == target:
                cnt += 1
            return 
        dfs(i+1, sum+numbers[i])
        dfs(i+1, sum-numbers[i])
    cnt = 0 
    dfs(0, 0)
    return cnt