def dfs(depth,lotto_list,idx,tlst):
    if depth == 6:
        res.append(tlst)
        return
    for i in range(idx,n):
            dfs(depth + 1,lotto_list,i + 1,tlst + [lotto_list[i]])





while True:
    lst = list(map(int,input().split()))
    n = lst[0]
    lotto_list = lst[1:]
    res = []
    dfs(0,lotto_list,0,[])
    for i in res:
        print(*i)
