
def get_time(line):
    line = list(line.split())
    hour, minute, second, millisecond = int(line[1][:2]), int(line[1][3:5]), int(line[1][6:8]), int(line[1][9:])
    t = float(line[2][:-1]) * 1000 - 1
    endTime = (hour * 60 * 60 * 1000) + (minute * 60 * 1000) + (second * 1000) + millisecond
    startTime = endTime - t

    return (startTime, endTime)

def solution(lines):
    answer = 0
    times = []

    for line in lines:
        times.append(get_time(line))

    for i in range(len(times)):
        cnt = 0
        for j in range(i, len(times)):
            if times[i][1] + 1000 > times[j][0]:
                cnt += 1

        answer = max(answer, cnt)
    return answer

# 로그 데이터 lines 배열에서 startTime, endTime을 구해 times 배열에 담아
# endTime을 밀리세컨드 단위로 나타내고, 처리 시간을 빼줘서 startTime을 구하면 된다.
# 이때, 문제에서 처리 시간은 시작 시간과 끝 시간을 포함한다고 했으므로 1을 더해준다.
# 그리고 초당 처리량을 구한다.
# 해당 구간에 처리하고 있는 로그의 수가 각각 로그의 endTime을 기준으로 변화하기 때문에, 처리량은 endTime 기준으로 구한다. 
# 구간은 endTime ~ endTime + 1000 - 1로 한다.
# 따라서 endTime + 1000 가  startTime 보다 크다면 해당 구간에서 처리하고 있다는 것을 의미하므로 cnt에 1을 더해준다.
# cnt값을 비교하며 가장 큰 값으로 answer를 갱신해준다.

# 손을 대는 게 부끄러운 문제 -> 1시간동안 쓴 코드를 다지워버렸다,,, 
# 추후 다시 디버깅해보기 **********