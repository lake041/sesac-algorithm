from itertools import product
def solution(word):
    answer = 0
    arr = []
    for i in range(1,6):
        for j in product('AEIOU', repeat=i):
            arr.append(''.join(j))
    arr.sort()
    for i, val in enumerate(arr):
        if val == word:
            return i+1