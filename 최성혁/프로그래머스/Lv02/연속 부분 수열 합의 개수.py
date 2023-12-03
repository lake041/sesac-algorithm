'''
    idx 1개씩 ~ len(elements)개씩 연속적으로 묶어 그 합을 set 자료형에 insert
    -> 어떻게 check?
    -> 리스트 값 하나씩 접근, lenth만큼 반복
    -> 자르는 경우는 len(elements)
'''
def solution(elements):
    result = set()
    length_elements = len(elements)
    elements = elements * 2
    for i in range(1, length_elements):
            for j in range(length_elements):
                    tmp = sum(elements[j:j + i:1])
                    result.add(tmp)
    # 마지막 값
    result.add(sum(elements))

    answer = len(result)

    return answer




print(solution([7,9,1,1,4]))
