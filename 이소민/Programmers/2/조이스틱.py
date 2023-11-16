# 복습 필요
def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(al):
        if ord(al) > 78:
            return 90-ord(al)+1
        else:
            return ord(al)-65

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer