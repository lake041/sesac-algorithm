def solution(elements):
    answer = 0
    return answer





lst = [7,9,1,1,4]*2	#18
lst2 = [set(),set(),set()]
for i in range(0, 5,1):
    
    lst2[0].add(sum(lst[i:i+2]))
    lst2[1].add(sum(lst[i:i+3]))
    lst2[2].add(sum(lst[i:i+4]))
    
print(lst2)