def solution(money):
    answer = 0

    n = len(money)

    # 처음 터는 경우
    dp = [[0, 0] for _ in range(n)]
    dp[0][1] = money[0]
    max_value = 0
    for idx in range(1, n):
        dp[idx][0] = max(dp[idx - 1][1], max_value)
        dp[idx][1] = dp[idx - 1][0] + money[idx]
        max_value = max(max_value, max(dp[idx]))

    answer = max(answer, dp[-1][0])

    # 처음 안터는 경우
    dp = [[0, 0] for _ in range(n)]
    max_value = 0
    for idx in range(1, n):
        dp[idx][0] = max(dp[idx - 1][1], max_value)
        dp[idx][1] = dp[idx - 1][0] + money[idx]
        max_value = max(max_value, max(dp[idx]))

    answer = max(answer, max(dp[-1]))

    return answer