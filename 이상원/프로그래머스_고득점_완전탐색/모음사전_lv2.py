from itertools import permutations, combinations, product
def solution(word):
    dic = ["A","E","I","O","U",""]
    lst = ["".join(j) for j in list(product(dic,repeat=5)) if j[0]!=""]
    lst = list(set(lst))
    lst.sort()
    for i in range(len(lst)):
        if word == lst[i]:
            return i+1





print(solution("AAAAE"))

for i in product([1,2,3,4], repeat=2):
    print(i, end=" ")



# dic = "123"
# lst = [j for j in list(permutations(dic,5)) if j[0]!=""]# 600
# lst = [j for j in list(permutations(dic,4)) if j[0]!=""]#300
# lst = [j for j in list(permutations(dic,3)) if j[0]!=""]#
# lst = [j for j in list(product(dic,repeat=5)) if j[0]!=""]#
# dic = ["A","E","I","O","U",""]
# lst = ["".join(j) for j in list(product(dic,repeat=5)) if j[0]!="" if "".join(j) not in lst]
# # lst = [j for j in list(permutations(dic,1)) if j[0]!=""]#5
# lst.sort()
# # a=""
# # lst2 = [j for i in permutations(dic,5) for j in i]
# print(len(lst))
# print(lst)

# lst = ["a","b"]

# print("".join(lst))

# a = "rgwg"
# a[0]="v"
# print(a)