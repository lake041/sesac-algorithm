def solution(arr):
    answer = 0
    tmp = 1
    m = max(arr)
    while 1:
        c = 1
        for a in arr:
            if (m*tmp)%a !=0:
                tmp+=1
                c=0
                break
        if c:
            return m*tmp
                
    # return 