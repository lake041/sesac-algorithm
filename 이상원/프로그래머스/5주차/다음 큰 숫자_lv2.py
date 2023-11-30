def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base) # num을 base로 나누고 몫, 나머지를 가져오는 divmod함수

    if q == 0:
        return temp[r]
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return convert(q, base) + temp[r]
    

def solution(n):
    answer = 0
    temp = str(convert(n, 2))
    cnt = 0
    cnt2 = 0
    for i in temp:
        if i =="1":
            cnt+=1
    for i in range (n+1,n*2,1):
        tmp = str(convert(i, 2))
        for j in tmp:
            if j =="1":
                cnt2+=1
        if cnt == cnt2:
            return i
        else:
            cnt2=0

print(solution(78))

temp = str(convert(78, 2))

print(temp)