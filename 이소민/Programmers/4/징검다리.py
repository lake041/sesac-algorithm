def solution(distance, rocks, n):
    answer = 0
    start = 1
    end = distance
    rocks.sort()
    while (start <= end):
        mid = (start+end)//2
        if diff(rocks, mid, distance) > n:
            end = mid -1
        else: 
            answer = mid
            start = mid +1
    return answer

def diff(rocks, mid, distance):
        before = 0
        after = distance
        cnt = 0
        for rock in rocks:
            if rock-before < mid:
                cnt+=1
            else:
                before = rock
        if after-before < mid:
            cnt +=1
        return cnt