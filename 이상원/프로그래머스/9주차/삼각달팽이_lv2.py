
# 방향을 전환하는 횟수가 n번임,,ㄷㄷ
# 방향전환은 처음 아래 -> 오른 -> 대각위->아래 -> 오른-> 대각위 로 계속 반복
# 즉 아래,오른,대각위가 반복되면 됨
def solution(n):
    answer = []
    triangle = [[0] * n for _ in range(n)] 
    x, y = -1, 0 # 처음엔 아래 방향 -> x=-1로 초기화
    curr = 1
    
    for i in range(n): # 방향 전환
        for _ in range(i, n): # 처음 아래로 갈때(i = 0)일때  n번 아래로 이동 / 그 다음 오른쪽으로 (i=1) 일때 n-i번 오른쪽 /
                                # 즉 방향전활 할때마다 n-(방향전환횟수) 만큼 이동함
            if i % 3 == 0: # 아래
                x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            elif i % 3 == 2: # 위쪽 대각선
                x -= 1
                y -= 1
            triangle[x][y] = curr
            curr += 1
    for i in triangle:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer


print(solution(4))