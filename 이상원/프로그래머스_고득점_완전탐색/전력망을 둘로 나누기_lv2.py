# 내 풀이
def solution(n, wires):
    tmp = wires.copy()
    # a ,b = []
    cnt = 0
    fir= [] 
    sec= []
    minus = 100
    while cnt<n-1:
        a,b = wires.pop(cnt)
        fir.append(a)
        sec.append(b)
        while len(fir)+len(sec)<n:
            for i in range(len(wires)):
                for j in fir:
                    if j in wires[i]:
                        fir = list(set(fir+wires[i]))
                for j in sec:
                    if j in wires[i]:
                        sec = list(set(sec+wires[i]))
        
        minus = min(minus, abs(len(fir)-len(sec)))
        fir = []
        sec = []
        cnt+=1
        wires=tmp.copy()
            
    return minus


# 다른 사람
def solution2(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]  # 집합연산자 & : 교집합 연산,   집합연산자 update : 여러데이터를 한번에 추가
        ans = min(ans, abs(2 * len(s) - n))
    return ans


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))

lst= [1,2,345]
s = set(lst)
s.update([3,4,1,2])

print(s)

# lst2 = lst.copy()
# lst2.pop()
# print(lst)
# print(lst2)