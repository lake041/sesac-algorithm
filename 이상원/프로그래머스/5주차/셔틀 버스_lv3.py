def solution(n, t, m, timetable):
    answer = ''
    new_timetable = []
    for i, time in enumerate(timetable):
        new_timetable.append( int(time[0:2])*60 + int(time[3:]) )
    new_timetable.sort(reverse = True)
    bus_table = [540+(i*t) for i in range(n)]
    
    anstmp = 0
    bus_idx = 0
    while bus_idx < len(bus_table):
        s_lst = []
        bus_onboard = 0
        while bus_onboard != m:
            if len(new_timetable) >= 1 and new_timetable[len(new_timetable)-1] <= bus_table[bus_idx]:
                bus_onboard += 1
                s_lst.append(new_timetable.pop())
            else:
                break
        if bus_idx == len(bus_table)-1:
            if bus_onboard == m:
                anstmp = s_lst.pop() - 1
            else:
                anstmp = bus_table[bus_idx]
        
        bus_idx += 1
    
    if anstmp//60 < 10:
        answer += '0'+str(anstmp//60)
    else:
        answer += str(anstmp//60)
    answer += ":"
    if anstmp%60 < 10:
        answer += '0'+str(anstmp%60)
    else:
        answer += str(anstmp%60)

    return answer



# n	t	m	timetable	                            answer
# 1	1	5	["08:00", "08:01", "08:02", "08:03"]	"09:00"
# 2	10	2	["09:10", "09:09", "08:00"]	"09:09"
# 2	1	2	["09:00", "09:00", "09:00", "09:00"]	"08:59"
# 1	1	5	["00:01", "00:01", "00:01", "00:01", "00:01"]	"00:00"
# 1	1	1	["23:59"]	"09:00"
# 10	60	45	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]	"18:00"

print(solution(1,	1,	5,	["08:00", "08:01", "08:02", "08:03"]))
l = ["31", "23", "135"]


def solution(n, t, m, timetable):
    answer = ''
    time=timetable.copy()
    for i in range(time):
        time.remove(timetable[i])