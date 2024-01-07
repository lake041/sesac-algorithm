def palindrome(s):
    if len(s) < 2 or s == s[::-1]:
        return True


def solution(s):

    if len(s) < 2 or s == s[::-1]:
        return len(s)

    for cur in range(len(s), 0, -1):
        for start in range(len(s)):
            currS = s[start: start + cur]
            if palindrome(currS):
                # result.append(len(s[start: start + cur]))
                return len(currS)
            if start + cur > len(s):
                break