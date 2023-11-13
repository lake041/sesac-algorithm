def solution(brown, yellow):
    resultList = []
    total = brown + yellow
    y = 3

    while True:
        if (total % y == 0):
            if (total // y - 2) * (y - 2) == yellow:
                resultList.append([total // y, y])

        y = y + 1

        if (total / y) < y:
            break

    return resultList[-1]