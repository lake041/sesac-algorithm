def solution(s):
    answer = True
    if s[0] == ')':
        return False

    stack = []
    stack.append(s[0])
    for i in range(1,len(s)):
        if s[i] == ')':
            if (len(stack)>0):
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])

    if len(stack) > 0:
        return False
    else:
        return True        



s = "(()("
lst = []
print(lst.pop())