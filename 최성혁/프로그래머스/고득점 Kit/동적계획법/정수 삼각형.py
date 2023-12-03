def solution(triangle):
    answer = 0
    dp = []
    # dp 테이블 초기화
    for i in range(len(triangle)):
        tmp = [0] * len(triangle[i])
        dp.append(tmp)
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[0][0] + triangle[1][0]
    dp[1][1] = triangle[0][0] + triangle[1][1]


    for i in range(2, len(triangle)):
        for j in range(len(triangle[i])):
            # 각 행의 첫번째 값은 비교 x
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][j]
            # 각 행의 마지막 값은 비교 x
            elif j == len(triangle[i]) - 1:
                dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
            # 각 행의 중간에 끼인 값은 비교
            else:
                dp[i][j] = max(triangle[i][j] + dp[i - 1][j - 1], triangle[i][j] + dp[i - 1][j])
    # dp 마지막 행의 최대값
    return max(dp[len(triangle) - 1])