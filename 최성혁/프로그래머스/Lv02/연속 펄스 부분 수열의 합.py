def solution(sequence):
    result = -1e9

    dp_table = [[0, 0] for _ in range(len(sequence))]

    dp_table[0][0], dp_table[0][1] = sequence[0] * -1, sequence[0]

    result = max(result, max(dp_table[0]))

    for idx, value in enumerate(sequence):
        if idx == 0:
            continue

        # Alternating sequence, so we need to switch signs.
        if idx % 2 == 0:
            dp_table[idx][0] = max(dp_table[idx - 1][0], 0) + sequence[idx] * -1
            dp_table[idx][1] = max(dp_table[idx - 1][1], 0) + sequence[idx]

        else:
            dp_table[idx][0] = max(dp_table[idx - 1][0], 0) + sequence[idx]
            dp_table[idx][1] = max(dp_table[idx - 1][1], 0) + sequence[idx] * -1

        result = max(result, max(dp_table[idx]))

    return result
