from collections import deque
from collections import defaultdict
import math
def solution(enroll, referral, seller, amount):
    answer = []
    m_level = defaultdict(str) # 나의 이름: [상급자이름, 나의 레벨]
    for i,j in zip(enroll, referral):
        if j == "-":
            m_level[i] = "center"
        else:
            m_level[i] = j

    income = defaultdict(int)
    q = deque(seller)
    a = deque(amount)
    while q:
        s = q.popleft()
        i = a.popleft()*100
        fee = math.trunc(i*0.1) # 낼 수수료 120
        income[s] += i-fee # 내가 번돈 중 90퍼 가져 1080
        lst = m_level[s] # 나의 상급자
        while lst != "": # 상급자가 없는 동안에
            # fee = math.trunc(i*0.1) # 낼 수수료
            income[lst] += fee - math.trunc(fee*0.1)  # 상급자에게 fee를 줘 108
            fee = math.trunc(fee*0.1) # 상급자의 상급자에게 줄 fee로 fee를 바까
            if fee < 1:
                break
            lst = m_level[lst] # lst를 나의 상급자로 바꿈

    for name in enroll:
        answer.append(income[name])

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	,["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary"],	[12, 4, 2, 5, 10]))






def solution2(enroll, referral, seller, amount):
    answer = []
    m_level = defaultdict(list) # 나의 이름: [상급자이름, 나의 레벨]
    for i,j in zip(enroll, referral):
        if j == "-":
            m_level[i] = ["center", 1]
        else:
            m_level[i] = [j, m_level[j][1]+1]


    
    income = defaultdict(int)
    refer = sorted(m_level.items(), key=lambda x:x[1][1], reverse=True) # 나의 레벨을 내림차순으로 정렬
    # print(refer)
    for ref in refer:
        m_fee = math.trunc(income[ref[0]]*0.1)# 하급자한테 받은 돈중 상급자한테 줄돈,
                                                        #즉 현재 가진돈 중 10%
        income[ref[0]] -= m_fee #현재돈 중 상급자한테 줄 돈 빼기
        income[ref[1][0]] += m_fee # 현재돈 중 상급자한테 줄 돈 주기
        if ref[0] in seller:# 내가 번돈 분배
            for i in range(len(seller)): 
                if ref[0] == seller[i]:
                    fee = math.trunc((amount[i]*100*0.1)) # 내가 번돈 중 상급자한테 줄돈
                    m_in = amount[i]*100 - fee # 내가 번돈 중 상급자한테 주고 남은 돈(내가가질돈)
                    income[ref[0]] += m_in
                    income[ref[1][0]] += fee

    # print(income)
    # print(enroll)
    
    for name in enroll:
        answer.append(income[name])

    return answer


# print(solution(["sw","john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	,["-","-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary","sw"],	[12, 4, 2, 5, 10,10]))


# d = defaultdict(int)
# d["q"] = 3

# print(d["q"]+5)

def solution3(enroll, referral, seller, amount):
    answer = []
    m_level = defaultdict(list) # 나의 이름: [상급자이름, 나의 레벨]
    for i,j in zip(enroll, referral):
        if j == "-":
            m_level[i] = ["center"]
        else:
            m_level[i] = [j]

    income = defaultdict(int)
    q = deque(seller)
    a = deque(amount)
    while q:
        s = q.popleft()
        i = a.popleft()*100
        fee = math.trunc(i*0.1) # 낼 수수료 120
        income[s] += i-fee # 내가 번돈 중 90퍼 가져 1080
        lst = m_level[s] # [나의 상급자]
        while lst != []: # 상급자가 없는 동안에
            # fee = math.trunc(i*0.1) # 낼 수수료
            income[lst[0]] += fee - math.trunc(fee*0.1)  # 상급자에게 fee를 줘 108
            fee = math.trunc(fee*0.1) # 상급자의 상급자에게 줄 fee로 fee를 바까
            lst = m_level[lst[0]] # lst를 나의 상급자로 바꿈

    for name in enroll:
        answer.append(income[name])

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	,["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary"],	[12, 4, 2, 5, 10]))
# print(solution2(["sw","john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	,["-","-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary","sw"],	[12, 4, 2, 5, 10,10]))



# a= defaultdict(list)

# print(a["ff"])


def solution3(enroll, referral, seller, amount):
    answer = []
    m_level = defaultdict(str) # 나의 이름: [상급자이름, 나의 레벨]
    for i,j in zip(enroll, referral):
        if j == "-":
            m_level[i] = "center"
        else:
            m_level[i] = j

    income = defaultdict(int)
    q = deque(seller)
    a = deque(amount)
    while q:
        s = q.popleft()
        i = a.popleft()*100
        fee = math.trunc(i*0.1) # 낼 수수료 120
        income[s] += i-fee # 내가 번돈 중 90퍼 가져 1080
        lst = m_level[s] # 나의 상급자
        while lst != "": # 상급자가 없는 동안에
            income[lst] += fee - math.trunc(fee*0.1)  # 상급자에게 fee를 줘 108
            fee = math.trunc(fee*0.1) # 상급자의 상급자에게 줄 fee로 fee를 바까
            if fee < 1:
                break
            lst = m_level[lst] # lst를 나의 상급자로 바꿈

    for name in enroll:
        answer.append(income[name])

    return answer

print(solution3(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	,["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary"],	[12, 4, 2, 5, 10]))