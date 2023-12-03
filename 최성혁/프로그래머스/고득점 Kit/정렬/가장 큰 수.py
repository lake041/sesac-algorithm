def solution(numbers):
    answer = ""
    # 처음 생각 모든 경우를 다 만들어서 max값 반환(X)

    # 숫자만 스트링으로 변환
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    # 1000 이하의 값이므로 3자리수 비교를위해 *3
    numbers = sorted(numbers, reverse=True, key=lambda x: x * 3)
    answer = answer.join(numbers)

    return str(int(answer))