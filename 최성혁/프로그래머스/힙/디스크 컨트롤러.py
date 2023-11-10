import heapq


def solution(jobs):
    answer = 0

    if len(jobs) == 1:
        return jobs[0][1]

    # 정렬
    jobs.sort(key=lambda x: (x[0], x[1]))

    # 진행
    q = []

    idx_job = 0
    now_time = jobs[0][0] + jobs[0][1]
    answer += jobs[0][1]
    idx_job = 1
    while 1:
        next_request_time, next_taken_time = jobs[idx_job][0], jobs[idx_job][1]

        # 요청받기
        if next_request_time <= now_time:
            heapq.heappush(q, (next_taken_time, next_request_time))
            idx_job += 1
        # 요청 더이상 넣을거 없는 경우
        else:
            if q:
                next_taken_time, next_request_time = heapq.heappop(q)
                now_time += next_taken_time
                answer += (now_time - next_request_time)

            else:
                now_time = next_request_time + next_taken_time
                answer += next_taken_time
                idx_job += 1

        if idx_job == len(jobs):
            break

    while q:
        next_taken_time, next_request_time = heapq.heappop(q)
        now_time += next_taken_time
        answer += (now_time - next_request_time)

    # 평균 계산
    answer //= len(jobs)

    return answer