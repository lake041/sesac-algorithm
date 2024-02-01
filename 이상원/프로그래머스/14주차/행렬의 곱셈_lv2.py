from itertools import product
from collections import deque
def solution(arr1, arr2):
    answer = [[0 for j in range(len(arr2))] for i in range(len(arr1))]
    lst = deque()
    for c in list(product(arr1, arr2)):
        temp = 0
        for i,j in zip(c[0], c[1]):
            temp+=i*j
        lst.append(temp)


    for x, y in product(len(answer), len(answer[0])):
        answer[x][y] = lst.popleft() 

    
    return answer


def solution(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]




a_var = [0,1,2,3,4]
b_var = [0,1,2,3]
c_var = [2,4,6,8]

print(zip(a_var,b_var,c_var)) # <zip object at 0x000001E3C0BA4340>
print(list(zip(a_var,b_var,c_var))) # [(0, 0, 2), (1, 1, 4), (2, 2, 6), (3, 3, 8)]
print(*list(zip(a_var,b_var,c_var))) # (0, 0, 2) (1, 1, 4) (2, 2, 6) (3, 3, 8) 
# * 붙으면 리스트나 튜플을 언팩

a = list(product([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))
print(a) # [([1, 4], [3, 3]), ([1, 4], [3, 3]), ([3, 2], [3, 3]), ([3, 2], [3, 3]), ([4, 1], [3, 3]), ([4, 1], [3, 3])]
# for c in a:
#     for i,j in zip(c[0], c[1]):
#         print(i*j)

# b = [i*j for i,j in zip(c[0], c[1]) for c in a]
# print(b)


SELECT fo.product_id
from FOOD_ORDER fo inner join food_product fp 
    on fo.product_id = fp.product_id 
where to_char(PRODUCE_DATE, 'yyyyMM') = '202205'
group by fo.product_id

P0022
P0023
P0024

286
448
578
977
1048