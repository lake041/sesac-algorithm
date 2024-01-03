def solution(line):
    answer, points = [], []

    for i in range(len(line)):
        a, b, e = line[i]

        for j in range(i + 1, len(line)):

            c, d, f = line[j]

            if a * d - b * c != 0 and (b * f - e * d) % (a * d - b * c) == 0 and (e * c - a * f) % (a * d - b * c) == 0:

                x = (b * f - e * d) // (a * d - b * c)
                y = -(e * c - a * f) // (a * d - b * c)

                if len(points) == 0:
                    top, bot = y, y
                    left, right = x, x
                else:
                    top = max(top, y)
                    bot = min(bot, y)
                    left = min(left, x)
                    right = max(right, x)

                points.append((x, y))

    for _ in range(top - bot + 1):
        answer.append(['.'] * (right - left + 1))

    for x, y in points:
        answer[y - bot][x - left] = '*'

    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])

    return answer