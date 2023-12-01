def solution2(elements):
    len_el = len(elements)
    lst=[set() for _ in range(len(elements)-1)]
    elements = elements*2
    
    for i in elements:
        lst[0].add(i)
    for i in range(0,len_el,1):
        for j in range(1,len_el-1,1):
            lst[j].add(sum(elements[i:i+j+1]))
    # answer = 0
    # for i in lst:
    #     answer += len(i)
    return lst
from sys import maxsize
# sequence는 비내림차순으로 정렬되어 있습니다.
def solution(sequence, k):
    anslst = []
    if k in sequence:
        x = sequence.index(k)
        return [x,x]
    # idx = k-1
    # if sequence[-1] > k:
    #     while 1:
    #         if idx not in sequence:
    #             idx -=1
    #         else:
    #             idx = sequence.index(idx)
    #             sequence = sequence[0:idx+1]
    #             break
    # sequence.reverse()
    # for i in range(len(sequence)-1, -1, -1):
    #     for j in range(i, -1, -1):
    #         sums = sum(sequence[i:j+1])
    #         if sums == k:
    #             anslst.append([j,i])
    #         elif sums > k:
    #             break
    # anslst.sort(key = lambda x:(len(x), x[0]))
    interval = maxsize
    for j in range(len(sequence)-1, -1, -1):
        for i in range(j, -1, -1):
            if interval < i-j+1:
                break
            sums = sum(sequence[i:j+1])
            if sums == k:
                anslst.append([i,j])
            elif sums > k:
                break
    anslst.sort(key=lambda x: (x[1]-x[0], x[0]))
    return anslst[0]


lst =[1, 1, 1, 2, 3, 4, 5,5]
print(solution(lst,5))