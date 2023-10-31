def solution(participant, completion):
    answer = ""
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(participant)):
        try:
            if participant[i] == completion[i]:
                continue
            else:
                answer = str(participant[i])
                return answer
        except:
            answer = str(participant[-1])
            return answer
            break
