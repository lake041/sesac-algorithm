def rotate(x1, y1, x2, y2):
    global matrix
    tmp1 = 0
    tmp2 = matrix[x1][y1 - 1]
    min_num = tmp2
    for i in range(y1, y2):
        tmp1 = matrix[x1 - 1][i - 1]
        matrix[x1 - 1][i - 1] = tmp2
        tmp2 = tmp1
        if (tmp2 < min_num):
            min_num = tmp2

    for i in range(x1, x2):
        tmp1 = matrix[i - 1][y2 - 1]
        matrix[i - 1][y2 - 1] = tmp2
        tmp2 = tmp1
        if (tmp2 < min_num):
            min_num = tmp2

    for i in reversed(range(y1, y2)):
        tmp1 = matrix[x2 - 1][i]
        matrix[x2 - 1][i] = tmp2
        tmp2 = tmp1
        if (tmp2 < min_num):
            min_num = tmp2

    for i in reversed(range(x1, x2)):
        tmp1 = matrix[i][y1 - 1]
        matrix[i][y1 - 1] = tmp2
        tmp2 = tmp1
        if (tmp2 < min_num):
            min_num = tmp2
    return min_num


def solution(rows, columns, queries):
    answer = []
    global matrix
    matrix = []
    num = 1
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(num)
            num += 1
    for query in queries:
        answer.append(rotate(query[0], query[1], query[2], query[3]))
    return answer