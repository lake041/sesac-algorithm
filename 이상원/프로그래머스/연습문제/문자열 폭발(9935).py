import sys

s = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

# while 1:
#     if b in s:
#         s = "".join(s.split(b))
#     else:
#         if s:
#             print(s)
#         else:
#             print("FRULA")
#         exit(0)



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
