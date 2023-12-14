from heapq import heappop, heappush
def solution(book_time):
    rooms = []
    book_time = sorted(book_time, key=lambda x: x[0])
    for book in book_time :
        check_in = num(book[0])
        check_out = num(book[1]) + 10
        if len(rooms) != 0 and rooms[0] <= check_in :
            heappop(rooms)
        heappush(rooms,check_out)
    return len(rooms)

def num(HHMM) :
    return 60*int(HHMM[:2]) + int(HHMM[3:])