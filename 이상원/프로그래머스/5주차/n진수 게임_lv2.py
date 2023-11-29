# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 
def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m*t):
        test += str(convert(i, n))
        
    for i in range(p,len(test),m):
        answer += test[i-1]
        if len(answer) == t:
            break
    return answer

# 10진수 -> n진수로 변환
def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base) # num을 base로 나누고 몫, 나머지를 가져오는 divmod함수

    if q == 0:
        return temp[r]
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return convert(q, base) + temp[r]
    

print(convert(300, 2))

print(solution(2,4,2,1))