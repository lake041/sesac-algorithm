def solution(numbers):
    answer = ''
    arr = []
    for i in numbers:
        i = str(i) + str(i) + str(i)
        arr.append(i)
    arr.sort(reverse=True)
    for i in arr:
        answer += i[:len(i)//3]
    return str(int(answer))