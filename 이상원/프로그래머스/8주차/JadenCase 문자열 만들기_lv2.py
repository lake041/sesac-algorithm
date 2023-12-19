def solution(s):
    answer = ''
    lst = s.split(' ')
    for l in range(len(lst)):
        if (lst[l] != '' and lst[l][0].isalpha()):
            answer += lst[l][0].upper()
            answer += lst[l][1:].lower()
        else:
            answer += lst[l].lower()
        
        if (l != len(lst)-1):
                answer += " "
                
    return answer


print(solution("abbr  gr grwq tbiwr 4sjrng 55fnie 56FNIENIW WWEEerji"))