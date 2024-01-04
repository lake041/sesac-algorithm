def solution(n):
    answer = []
    def hanoi(n,a,b,c):
        if n == 1:
            answer.append([a,c])
            return answer
        hanoi(n-1, a,c,b)
        answer.append([a,c])
        hanoi(n-1, b,a,c)
    hanoi(n,1,2,3)
    return answer