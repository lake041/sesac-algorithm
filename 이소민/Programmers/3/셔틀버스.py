def solution(n, t, m, timetable):
    answer = ""
    crews = [] 

    for time in timetable:
        minute = int(time[:2]) * 60 + int(time[3:5])
        crews.append(minute)
    crews.sort()  

    departure = 540 
    index = 0 
    corn_time = 0

    for i in range(1, n+1):
        ride = 0 
        for j in range(index, len(crews)):
            if crews[j] > departure:
                break
            if crews[j] <= departure: 
                ride += 1
                index += 1
                if ride == m:
                    break

        if i == n:
            if ride == m:
                corn_time = crews[index-1] - 1
            else:
                corn_time = departure

        departure += t

    if corn_time // 60 < 10:
        answer += "0"
    answer += str(corn_time // 60) + ":"

    if corn_time % 60 < 10:
        answer += "0"
    answer += str(corn_time % 60)

    return answer
