from heapq import heappop, heappush

def solution(book_time):
    rooms = []
    book_time.sort(key = lambda _:_[0])
    for book in book_time :
        check_in = num(book[0])
        check_out = num(book[1]) + 10
        if len(rooms) != 0 and rooms[0] <= check_in :
            heappop(rooms)
        heappush(rooms,check_out)
    return len(rooms)

def num(HHMM) :
    return 60*int(HHMM[:2]) + int(HHMM[3:])

from heapq import heappop, heappush

def solution2(book_time):
    answer = 1
    
    # "HH:MM" → HH * 60 + MM
    book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_ref.sort()
    
    heap = []
    for s, e in book_time_ref:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)
    
    return answer


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution2([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))