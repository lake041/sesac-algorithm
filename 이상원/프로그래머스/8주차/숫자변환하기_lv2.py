def solution(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)
    
    while dp:
        if y in dp:
            return answer
        else:
            dp_y = set()
            for i in dp:
                if i+n <= y:
                    dp_y.add(i+n)
                if i*2 <= y:
                    dp_y.add(i*2)
                if i*3 <= y:
                    dp_y.add(i*3)
            dp = dp_y
            answer += 1
            
    return -1


def solution2(x, y, n):
    ans = 10000000
    c = 0
    while int((y-(c*n))/x) > 0:
        a = 0
        b = 0
        temp = ((y-(c*n))/x)
        while 1:
            if temp%2==0:
                temp=int(temp/2)
                a+=1
            elif temp%3 == 0:
                temp=int(temp/3)
                b+=1
            else:
                break
        if temp != 1:
            c +=1
            continue    
        d = (2**a)*(3**b)
        if ((y-(c*n))/x)==d:
            ans = min(ans, a+b+c)
            print("a =", a)
            print("b =", b)
            print("c =", c)
        c +=1
    if ans == 10000000:
        return -1
    
    return ans

print(solution(10,	40,	5))
# print(solution(10,	40,	30))
# print(solution(2,	5,	4))
# 10	40	5	2
# 10	40	30	1
# 2	5	4	-1

# from collections import defaultdict
# def insubunhae(n):
#     dic = defaultdict(int)
#     while 1:
#         if n%3==0:
#             n=n/3
#             dic["3"] +=1
#         elif n%2 == 0:
#             n=n/2
#             dic["2"] +=1
#         else:
#             dic["n"] += int(n)
#             return dic

# def sik(a,b,c,n):
#     return ((2**a)*(3**b))+(n*c)

# print(insubunhae(40))


#     return answer

# print(solution(10, 100, 5)) #3*3+2*5
# /2 /2 -5 /2 










def solution1(x, y, n):
    answer = 0
    if y%x !=0:
        return -1
    while 1:
        if y%3==0:
            y=min(y/3, y-n)
            answer+=1
        elif y%2 == 0:
            y=min(y/2, y-n)
            answer += 1
        else:
            y-=n
            answer += 1
        if y == x:
            return answer
        if y < x:
            return -1 