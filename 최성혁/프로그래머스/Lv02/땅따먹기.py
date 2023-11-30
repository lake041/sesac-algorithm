'''
1) 테케 통과 -> 전부 실패
'''
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            # 이전 행에서 현재 열을 제외한 최대값을 현재 위치에 더해줌
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    # 마지막 행에서 가장 큰 값이 최종 결과
    answer = max(land[-1])
    return answer



print(solution([[0,0,0,0],[0,0,0,0],[0,0,0,0]]))

