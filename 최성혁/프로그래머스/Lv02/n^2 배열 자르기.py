def solution(n, left, right):
    result = []

    for i in range(left // n, right // n + 1):
        row = i + 1
        for j in range(n):
            col = j + 1
            value = max(row, col)
            result.append(value)

    return result[left % n: (right % n) + 1]
