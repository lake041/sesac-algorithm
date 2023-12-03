def dfs(start,answer,visited,tickets):
    visited[start] = True
    for i in range(len(tickets)):
        if visited[i] == False and tickets[start][1] == tickets[i][0]:
            answer.append(tickets[i][1])
            dfs(i,answer,visited,tickets)




def solution(tickets):
    # DFS
    answer = []

    # 방문배열
    visited = [False] * len(tickets)

    # 두 번째 값으로 정렬
    tickets.sort(key = lambda x:x[1])

    # "ICN" 개수 구하기
    icncount = 0
    flag = True
    for i in tickets:
        if i[0] == "ICN" or i[1] == "ICN":
            icncount += 1
        if icncount >= 2:
            flag = False
            break

    # 정렬 후
    if flag == False and tickets[0][0] != "ICN":
        for i in range(1,len(tickets)):
            if tickets[i][0] == "ICN":
                tickets[0],tickets[i] = tickets[i],tickets[0]
    elif flag == True:
        for i in range(1,len(tickets)):
            if tickets[i][0] == "ICN":
                tickets[0],tickets[i] = tickets[i],tickets[0]

    # 처음 나온 티켓들 answer에 append
    answer.append(tickets[0][0])
    answer.append(tickets[0][1])

    # dfs 시작
    for i in range(len(tickets)):
        if visited[i] == False:
            dfs(i,answer,visited,tickets)

    return answer
