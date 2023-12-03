def solution(clothes):
    result = dict()
    for item in clothes:
        clothing_type = item[1]
        if clothing_type in result:
            result[clothing_type] += 1
        else:
            result[clothing_type] = 1
    answer = 1

    for value in result.values():
        answer *= (value + 1)

    answer -= 1

    return answer