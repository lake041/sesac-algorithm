n,m = map(int,input().split())
visited = [False] * (n+1)
answer = []

def dfs(start,lst):
    if start == m:
        for i in range(len(lst)):
            print(lst[i],end=" ")
        print()
        return

    for j in range(1,n+1):
        if visited[j] == False:
            visited[j] = True
            dfs(start + 1, lst + [j])  # 숫자 뒤에 공백 추가
            visited[j] = False









lst = []
dfs(0,lst)
