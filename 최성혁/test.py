from collections import deque
a = deque([1,1,2,3,4])
b = [1,2,2,5,7,8]


for i in range(len(a)):
    if a[i] not in b:
        print(a[i])
