def solution(elements):
    len_el = len(elements)
    lst=set()
    elements = elements*2
    
    for i in elements:
        lst.add(i)
    for i in range(0,len_el,1):
        for j in range(1,len_el-1,1):
            lst.add(sum(elements[i:i+j+1]))
    
    return len(lst)+1



lst = [7,9,1,1,4]
print(solution(lst))
# lst = [7,9,1,1,4]*2	#18
# lst2 = [set(),set(),set()]
# for i in range(0, 5,1):
    
#     lst2[1].add(sum(lst[i:i+2]))
#     lst2[2].add(sum(lst[i:i+3]))
#     lst2[3].add(sum(lst[i:i+4]))
    
# print(lst2)