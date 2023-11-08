import heapq
import math
# 첫 작업이 끝나고 다음 작업 고르는 기준 -> 현재 시점에 처리할 수 있는 것중에 가장 시간이 짧게 걸리는 것 부터 실행
# 겹치는 시간이 없으면 바로 다음것을 실행한다
# 평균을 구하고 소수점은 버린다


def solution(jobs):
    answer = 0
    n = len(jobs)
    now = 0
    start = -1
    curr_pro_able = [] # 현재(now) 처리할 수 있는 작업 리스트
    cnt = 0
    while True:
        if (cnt == n):
            break
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(curr_pro_able, [job[1], job[0]])
                #현재 작업할 수 있는 프로세스 테이블에 (소요시간, 요청시간) 순으로 넣어서 소요시간이 가장 작은 것이 첫 번째로 오도록 힙을 만듬
        if curr_pro_able:
            protime,reqtime = heapq.heappop(curr_pro_able)
            start = now
            cnt+=1
            now += protime
            answer += (now - reqtime)
        else:
            now+=1

    return answer//n
lst = [[0, 3], [1, 9], [2, 6]]
print(solution(lst))

def solution2(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)


# 처음 푼 답 -> 오답 - 프로세스가 끝난 후 다음 프로세스를 선택하는 기준을 잘못 설정해서 테스트케이스만 성공함
def solution3(jobs):
    answer = 0
    n = len(jobs)
    heapq.heapify(jobs)
    
    hard_rest = True
    currtime = 0
    sum_req_end = 0
    while jobs:
        
        # currtime+=time
        if hard_rest:
            req,time = heapq.heappop(jobs)
            if req <0:
                req *=-1
            hard_rest = False
            currtime += time
            sum_req_end += currtime-req
        else:
            if currtime<=jobs[0][0]:
                hard_rest = True
                continue

            times = [0]*len(jobs)
            for i in range(len(jobs)):
                times[i] = [jobs[i][1]+(currtime-jobs[i][0]), i]
            heapq.heapify(times)
            a, b = heapq.heappop(times)
            jobs[b][0] *= -1
            heapq.heapify(jobs)
            hard_rest = True


    return sum_req_end//n 