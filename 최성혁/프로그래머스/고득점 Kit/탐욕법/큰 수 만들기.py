def solution(number, k):
    answer = ''
    index = -1
    for i in range(0, len(number)-k):
        max_num = '0'
        for idx in range(index+1, k+i+1):
            if(max_num < number[idx]):
                index = idx;
                max_num = number[idx]

        answer += max_num

    return answer