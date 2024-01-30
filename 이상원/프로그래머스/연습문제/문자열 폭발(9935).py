import sys

s = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

r = []
for i in s:
    r.append(i)
    if i == b[-1] and r[-len(b):] == list(b):
        for _ in range(len(b)):
            r.pop()

if r:
    print("".join(r))
else:
    print("FRULA")
