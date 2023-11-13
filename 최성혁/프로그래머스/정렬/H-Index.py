def solution(citations):
    answer = 0
    '''
    각 요소별 의미 : 논문의 인용 횟수
         [0,1,3,5,6]
     i  = 4 3 2 1 0   
     il = 1 2 3 4 5
    '''
    citations.sort()

    for i in range(len(citations)):
        citationsLength = len(citations) - i
        print(citationsLength)
        if citations[i] >= citationsLength:
            return citationsLength
    return 0