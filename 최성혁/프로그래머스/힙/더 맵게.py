def solution(scoville, K):
    scoville.sort()
    mix_count = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        first = scoville.pop(0)
        second = scoville.pop(0)
        new_scoville = first + (second * 2)
        scoville.insert(0, new_scoville)
        scoville.sort()
        mix_count += 1

    return mix_count

