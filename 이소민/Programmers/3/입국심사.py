def solution(n, times):
    answer = 0
    times.sort()
    start = times[0]
    end = times[-1]*n
    while(start <= end):
        mid = (start+end) // 2
        total = 0
        for time in times:
            total += mid//time
        if total < n:
            start = mid+1
        else:
            end = mid-1
            answer = mid
    return answer