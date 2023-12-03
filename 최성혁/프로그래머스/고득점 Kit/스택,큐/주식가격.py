def solution(prices):
    remaining_time = []

    for i in range(len(prices)):
        duration = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                duration = j - i
                break
            duration = j - i
        remaining_time.append(duration)

    return remaining_time


