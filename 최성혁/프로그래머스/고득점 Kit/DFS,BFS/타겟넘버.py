count = 0
def dfs(numbers,level,target,sum):
    global count
    if len(numbers) == level:
        if target == sum:
            count += 1
        return
    dfs(numbers,level+1,target,sum + numbers[level])
    dfs(numbers,level+1,target,sum - numbers[level])


def solution(numbers, target):

    dfs(numbers,0,target,0)
    return count
