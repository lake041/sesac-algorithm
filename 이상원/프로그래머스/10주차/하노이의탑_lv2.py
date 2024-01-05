from collections import deque
def solution(n):
    answer = []
    top1=[i for i in range(n,0,-1)]
    top2, top3 = [],[]
    q = deque([top1, top2, top3, answer])
    visited = [[top1, top2, top3]]
    while q:
        top1, top2,top3, ans = q.popleft()
        if top1 ==[] and top2 ==[]:
            return ans
        if top1:
            pop = top1.pop()
            if not top2 or top2[-1] > pop:
                top2.append(pop)
                if [top1, top2,top3] not in visited:
                    q.append([top1, top2,top3, ans+[1,2]])
                    visited.append([top1, top2,top3])
            if not top3 or top3[-1] > pop:
                top3.append(pop)
                if [top1, top2,top3] not in visited:
                    q.append([top1, top2,top3, ans+[1,3]])
                    visited.append([top1, top2,top3])
            
        
        

                
    return answer


from collections import deque
def solution2(n):
    top = [[0 for i in range(3)] for j in range(n)]
    for i in range(n):
        top[i][0]= i+1
    print(top)




def solution3(n):
    answer = []
    
    def hanoi(src, tgt, inter, n): # 인자 순서 넣어주는 게 좀 헷갈렸음.
        if n == 1:
            answer.append([src, tgt])
        else:
            hanoi(src,inter,tgt,n-1)
            hanoi(src,tgt,inter,1)
            hanoi(inter,tgt,src,n-1)
            
    hanoi(1,3,2,n)
    
    return answer



def solution4(n):
    dp = [0 for i in range(n+1)]
    dp[1] =1
    dp[2] =3
    for i in range(3,n+1):
        dp[i] = dp[i-1] *2 +1
    
    return dp[n]
print(solution4(5))