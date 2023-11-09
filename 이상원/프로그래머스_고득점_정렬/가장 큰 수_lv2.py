def solution(numbers):
    answer = ''
    lst = []
    for i in range(len(numbers)):
        num = numbers[i]
        lst.append(str(num))
    lst.sort(key=lambda x: x*3, reverse=True)

    for a in lst:
        answer+=a
    if (answer[0]) == "0":
        return "0"    
    return answer

lst = [0,0]

print(solution(lst))
# lst.sort(reverse=True)



print(lst)
# lst.sort(key=lambda k:k[0])
