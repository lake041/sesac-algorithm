# 실패코드
# def solution(elements,k):
#
#     length_elements = len(elements)
#
#     resultList = dict()
#     # 딕셔너리 초기화
#     for i in range(length_elements):
#         resultList[i] = 0
#
#     for i in range(1,length_elements):
#         for j in range(length_elements - (i-1)):
#             tmp = sum(elements[j:j + i:1])
#             if tmp == k:
#                 length = len(elements[j:j + i:1])
#                 if resultList[length] == 0:
#                     resultList[length] = [j,(j+i)-1]
#
#     for val in resultList.values():
#         if val != 0:
#             return val
#
#
#
# print(solution([2, 2, 2, 2, 2],6))

def solution(sequence, k):
    answer = []
    start, end = 0,0
    temp = sequence[0]
    min_len = 1000001

    while start <= end < len(sequence):
        if temp == k :
            if end - start + 1 < min_len :
                min_len = end - start + 1
                answer = [start, end]
            temp -= sequence[start]
            start += 1

        elif temp < k :
            end += 1
            if end < len(sequence) :
                temp += sequence[end]

        elif temp > k :
            temp -= sequence[start]
            start += 1

    return answer