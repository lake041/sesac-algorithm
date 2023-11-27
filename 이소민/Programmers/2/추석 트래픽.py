from datetime import datetime, timedelta

def solution(lines):
    answer = 0
    startAt, finishAt = [], []
    
    for line in lines:
        date_str, time_str, duration_str = line.split()
        time = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M:%S.%f")
        duration = timedelta(seconds=float(duration_str[:-1]))
        
        finishAt.append(time)
        startAt.append(time - duration + timedelta(milliseconds=1))
    
    for i in range(len(finishAt)):
        count = 0
        finishAt[i] += timedelta(seconds=1)
        
        for j in range(i, len(startAt)):
            if startAt[j] < finishAt[i]:
                count += 1
                
        answer = max(answer, count)
        
    return answer
