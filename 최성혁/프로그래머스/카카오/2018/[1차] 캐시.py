def solution(cacheSize, cities):
    LRUQ = []
    answer = 0

    # 대소문자 구분 X -> 모두 소문자로
    cities = [city.lower() for city in cities]

    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        # 꽉 차있을경우
        if len(LRUQ) == cacheSize:
            tmp = ""
            # Hit
            if i in LRUQ:
                for idx, target in enumerate(LRUQ):
                    if target == i:
                        tmp = LRUQ.pop(idx)
                        break
                LRUQ.insert(0, tmp)
                answer += 1
            # miss
            else:
                LRUQ.pop()
                LRUQ.insert(0, i)
                answer += 5
        # 꽉 안차있는경우
        else:
            # Hit
            if i in LRUQ:
                for idx, target in enumerate(LRUQ):
                    if target == i:
                        tmp = LRUQ.pop(idx)
                        break
                LRUQ.insert(0, tmp)
                answer += 1
            # miss
            else:
                LRUQ.insert(0, i)
                answer += 5

    return answer

print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
