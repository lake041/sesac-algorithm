def solution(arr):
    answer = [0,0]
    len_arr = len(arr)
    def fourSame(r,c,l): #r=row c=column l=length
        start= arr[r][c] 
        for i in range(r,r+l):
            for j in range(c,c+l):
                if arr[i][j] != start: #  arr이 모두 같은지 봄 -> 다르면 4영역으로 나눠서 다시 ㄱㄱ
                    l =  l//2 
                    fourSame(r,c,l)
                    fourSame(r+l, c,l)
                    fourSame(r,c+l,l)
                    fourSame(r+l,c+l,l)
                    return # 다르면 돌리고 바로 함수 종료시켜줘야댐 (break 쓰면 j루프만 종료된다구!)
        
        answer[start] +=1
    
    fourSame(0,0,len_arr)
            
    return answer




