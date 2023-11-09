def solution(array, commands):
    answer = []
    for com in commands:
        lst = array[com[0]-1:com[1]]
        lst.sort()
        answer.append(lst[com[2]-1])
    return answer

l, r =[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(l,r))