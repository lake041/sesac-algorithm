def solution(s):
    answer = True
    stack = []
    for i in s:
        if len(stack) == 0:
            if i == ")":
                return False
            else:
                stack.append(i)
        elif len(stack) != 0:
            if stack[-1] == i:
                stack.append(i)
            else:
                stack.pop()
    if len(stack) != 0:
        return False

    return True

# [level 2] Title: 올바른 괄호, Time: 10.62 ms, Memory: 10.4 MB