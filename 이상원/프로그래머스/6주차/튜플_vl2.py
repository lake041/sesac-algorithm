from collections import defaultdict
def solution(s):
    answer = []
    d = defaultdict(int)
    temp = ""
    for k in s:
        if k.isnumeric():
            temp += k
        else:
            if temp != "":
                d[temp] += 1
                temp = ""
    
    answer = [ int(x) for x,i in sorted(d.items(), key= lambda x: x[1], reverse=True)]
    

    

    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))