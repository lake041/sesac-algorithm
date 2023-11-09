def solution(citations):
    answer = 0
    n = len(citations)
    h = []
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] > i:
            h.append(i+1)
        
    if h:
        return max(h)
    else:
        return 0        
    

f = [1,1,1,1,1,1]
# f= [0,0,0,0,0]
f = [10,8,5,4,3]
# f=  [9,7,6,2,1]
print(solution(f))
# n = len(f)
# f.sort(reverse=True) # [6, 5, 3, 1, 0]
# if f[4] >= 4
# print(f)
# print(citations[n//2])