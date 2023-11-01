participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

participant = sorted(participant)
completion = sorted(completion)
answer = ""
for i in range(len(participant)):
    try:
        if participant[i] == completion[i]:
            continue
        else:
            answer = str(participant[i])
            print(answer)
            break
    except:
        answer = str(participant[-1])
        print(answer)
        break
