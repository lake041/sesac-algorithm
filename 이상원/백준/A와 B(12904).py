# from collections import deque
# fir, tar = input(), input()
# q = deque()
# q.append(fir)
# while q:
#     pop = q.popleft()
#     if len(pop) > len(tar):
#         print(0)
#         break
#     if pop not in tar:
#         continue
#     if pop == tar:
#         print(1)
#         break
#     n = pop + "A"
#     tmp = reversed(list(pop))
#     rev = "".join(tmp)
#     rev += "B"
#     if n == tar or rev == tar:
#         print(1)
#         break
#     q.append(pop+"A")
#     q.append(rev)
# else:
#     print(0)


S = input()
T = input()

flag = False

while len(S) <= len(T):
    if S != T:
        # 뒤에 A 삭제
        if T[-1] == 'A':
            T = T[:-1]
        # B 삭제 후 뒤집기
        else:
            T = T[:-1]
            T = T[::-1]
    else:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)