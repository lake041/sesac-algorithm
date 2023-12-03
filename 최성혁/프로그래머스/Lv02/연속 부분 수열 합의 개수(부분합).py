def solution(elements):
    n = len(elements)
    accum = [0] * (n + 1)

    for i in range(1, n + 1):
        accum[i] = accum[i - 1] + elements[i - 1]
    print(accum)
    result_set = set()

    for size in range(1, n + 1):
        start = 1
        end = start + size - 1

        while start <= n:
            if end < start:
                result_set.add(accum[end] + accum[n] - accum[start - 1])
            else:
                result_set.add(accum[end] - accum[start - 1])

            start += 1
            end += 1

            if end == n + 1:
                end = 1

    return len(result_set)


# Example usage:
elements = [7, 9, 1, 1,4]
result = solution(elements)
print(result)
