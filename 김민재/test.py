from collections import Counter

x = [1, 2, 3, 3]
print(x.count(3))

counter = Counter(x)
x = []
print(counter)