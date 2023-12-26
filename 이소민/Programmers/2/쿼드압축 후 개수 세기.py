def solution(arr):
    answer = [0,0]
    def re(a,b,l):
        tmp = arr[a][b]
        for i in range(a,a+l):
            for j in range(b, b+l):
                if arr[i][j] != tmp:
                    l = l//2
                    re(a,b,l)
                    re(a,b+l,l)
                    re(a+l,b,l)
                    re(a+l, b+l, l)
                    return
        answer[tmp] += 1
    re(0,0,len(arr))
    return answer