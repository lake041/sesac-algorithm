from string import ascii_lowercase
import math
from collections import Counter
def solution(str1, str2):
    answer = 0
    alp_lst = list(ascii_lowercase) # isalpha 함수가 있었음,,,ㄷㄷ
    lst_str1 = ["" for _ in range(len(str1)-1)]
    lst_str2 = ["" for _ in range(len(str2)-1)]
    for i in range(len(str1)-1):
        if str1[i].lower() in alp_lst and str1[i+1].lower() in alp_lst:
            lst_str1[i]=(str1[i]+str1[i+1]).lower()

    for i in range(len(str2)-1):
        if str2[i].lower() in alp_lst and str2[i+1].lower() in alp_lst:
            lst_str2[i]=(str2[i]+str2[i+1]).lower()
    
    
    # set1, set2 = set(lst_str1), set(lst_str2)

    Counter1 = Counter(lst_str1)
    Counter2 = Counter(lst_str2)
    
    gyo = list((Counter1 & Counter2).elements())
    hap = list((Counter1 | Counter2).elements())
    
    if len(hap) == 0 and len(gyo) == 0:
        return 65536
    else:
        return int(len(gyo) / len(hap) * 65536)



str1, str2 = "FRANCE".lower(),"french"
print(solution(str1,str2))
set1, set2 = set(str1), set(str2)
print((len(set1 & set2)/len(set1 | set2))*65536)
print()


A = [1, 1, 2, 2, 3]
B = [1, 2, 2, 4, 5] 

set1, set2 = set(A), set(B)
print(set1|set2)

#A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}
# print("A".lower())


from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)