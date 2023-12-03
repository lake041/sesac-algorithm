def solution(sequence, k):
    answer = []
    s = 0
    e = 0
    l = len(sequence)    
    sum_ = 0
    while True:
        if sum_ <= k:
            if sum_ == k:
                answer.append([s, e-1])
            if e >= l: break
            sum_ += sequence[e]
            e += 1
        else:
            sum_ -= sequence[s]
            if s >= l: break
            s += 1
    answer = sorted(answer, key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]