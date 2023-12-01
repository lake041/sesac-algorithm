def solution(land):
    answer = 0

    # 첫 번째 생각
    # n행의 최댓값의 인덱스와 n+1행의 최댓값의 인덱스 겹치지 않으면 n행에서 최댓값을 선택한다.
    # 겹치는 경우는 n행에서 차선책 + (n+1)행의 최선책과 n행에서의 최선책 + (n+1)행의 차선책의 값과 비교하여 n행에서의 값을 선택한다

    # -> 개빡치게 테케만 통과하고 하나도 안맞음


    for i in range(len(land)-1):
        n_max = max(land[i])
        n1_max = max(land[i+1])
        n_max_idx = land[i].index(n_max)
        n1_max_idx = land[i+1].index(n1_max)
        ans = 0
        if n_max_idx != n1_max_idx:
            ans = n_max
            land[i+1][n_max_idx] = 0
            answer+=ans
        else:
            temp = land[i].copy()
            temp[n_max_idx] = 0
            n_sec = max(temp)
            temp = land[i+1].copy()
            temp[n1_max_idx] = 0
            n1_sec = max(temp)
            if n_sec + n1_max > n_max + n1_sec:
                ans = n_sec
                answer += ans
            else:# n_sec + n1_max <= n_max + n1_sec:
                ans = n_max
                answer += ans
            land[i+1][land[i].index(ans)] =0 
        # if i == len(land)-2:
        #     land[i+1][land[i].index(ans)] =0

    answer+=max(land[-1])


    return answer


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))


def solution2(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    return max(land[len(land) - 1])

from itertools import product
def solution3(land):
    for i,j in product(range(1, len(land)), range(len(land[0]))):
        land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    return max(land[-1])

# n-1 행을 돌면서 인덱스[j]값을 제외한 최댓값을 n행 인덱스[j]에 더해줌
# 프로덕트 적용해 봄
# 생각보다 허무하게 쉬우면서 생각해내기 어려운듯한 dp 문제,,,


print(solution2([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

print(solution3([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))