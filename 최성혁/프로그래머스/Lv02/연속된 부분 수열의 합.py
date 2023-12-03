def solution(elements,k):

    length_elements = len(elements)

    resultList = dict()
    # 딕셔너리 초기화
    for i in range(length_elements):
        resultList[i] = 0

    for i in range(1,length_elements):
        for j in range(length_elements - (i-1)):
            tmp = sum(elements[j:j + i:1])
            if tmp == k:
                length = len(elements[j:j + i:1])
                if resultList[length] == 0:
                    resultList[length] = [j,(j+i)-1]

    for val in resultList.values():
        if val != 0:
            return val



print(solution([2, 2, 2, 2, 2],6))