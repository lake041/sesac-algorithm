from collections import defaultdict
def solution(picks, minerals):
    answer = 0
    cnt = 0
    # minerals = ["diamond", "diamond","iron", "stone", "diamond", "iron", "iron", "diamond", "iron", "stone","diamond", "iron", "stone","diamond", "iron", "stone","iron", "stone","diamond", "iron", "stone","diamond", "iron", "stone","stone","diamond","stone","diamond",]
    for i in picks:
        cnt += i # 4
    minerals= minerals[:cnt*5] # 4 * 5 minerals[:20]
    lst = []
    lst2 = []
    dic = defaultdict(int) # 각 광물을 캐는데 드는 최대 피로도
    dic["diamond"] = 25
    dic["iron"] = 5
    dic["stone"] = 1
    for i in range(0,len(minerals),5):
        temp = minerals[i:i+5] #0~5, 5~10 10~15 
        lst2.append(minerals[i:i+5])
        for j in range(len(temp)):
            temp[j] = dic[temp[j]]
        lst.append(temp)
    lst.sort(key = lambda x:sum(x), reverse=True)
    for i in range(len(lst)):
        div = 1
        if picks[0]:
            div = 25
            picks[0] -= 1
        elif picks[1]:
            div = 5
            picks[1] -= 1
        else:
            picks[2] -= 1
        for j in lst[i]:
            if j/div < 1:
                answer += 1
            else:
                answer += int(j)/div

    return answer

print(solution([0,1,3], ["iron","stone","iron","stone","iron","iron","iron","iron","iron","iron"]))







## 성혁 코드(정답 아님)
from collections import deque
def solution(picks, minerals):
    answer = 0
    mineralq = deque(minerals)
    breakFlag = True

    cnt = 0

    for i in range(len(picks)):
        picks[i] *= 5

    for i in picks:
        if i == 0:
            pass
        # 현재 곡괭이
        for j in range(i):
            if not mineralq:
                breakFlag = False
                break
            target = mineralq.popleft()
            if target == "diamond":
                if cnt == 0:
                    answer += 1 
                elif cnt == 1:
                    answer += 5
                else:
                    answer += 25
            elif target == "iron":
                if cnt == 2:
                    answer += 5
                else:
                    answer += 1
            elif target == "stone":
                answer += 1

        if breakFlag == False:
            break

        cnt += 1 

    return answer

# print(solution([0,1,3], ["iron","stone","iron","stone","iron","iron","iron","iron","iron","iron"]))