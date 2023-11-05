from collections import deque
# def solution(tickets):
    
#     q = deque()
#     templst = []
#     for tic in tickets:
#         if tic[0] == "ICN":
#             templst.append(tic)
#     templst.sort()
#     answer = ["ICN", templst[0][1]]
#     tickets.remove(templst[0])
#     v = [[0,0] for i in range(len(tickets))]
#     q.append(templst[0])
#     while q:
#         arr, dep = q.popleft()
#         for i in range(len(tickets)):
#             if not v[i][] and tickets[i][0] == dep:
#                 q.append(tickets[i])
#                 answer.append(tickets[i][1])
#                 v[i][0] = 1
                    
        



#     return answer


def solution(tickets):
    q = deque()
    q.append([["ICN"], tickets.copy()])
    answer =[]
    answerlist= []
    while q:
        ans, tic = q.popleft()
        if len(tic) == 0:
            answerlist.append(ans);
            continue
    
        for i in range(len(tic)):
            tic_ifirst = tic[i][0]
            tic_isecond = tic[i][1]    
            anslastval = ans[-1]

            if tic_ifirst == anslastval:
                # ans.append(tic_isecond)
                # tic.remove([anslastval, tic_isecond])
                temp_ans = ans[:]
                temp_ans.append(tic_isecond)
                temp_tic = tic[0:i]+tic[i+1:]
                q.append([temp_ans, temp_tic])
                


    answerlist.sort()
    return answerlist[0]

lst  =[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
lst2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

# lst = ["wef", "wfeggg", "wrgj", "wekfn"]

# lst2= lst[0:0] + lst[4:]
# temp_ans = lst[:]
# print(temp_ans)
print(solution(lst2))

# ["ICN", "ATL"]
# ["ATL", "ICN"],    ["ATL","SFO"]
# ["ICN", "SFO"]     ["SFO", "ATL"]
# ["SFO", "ATL"]     ["ATL", "ICN"]              
# ["ATL", "ICN"]     ["ICN", "SFO"]


# ["SFO", "ATL"]
# ["ATL","SFO"]
# v = [[0,0] for i in range(len(lst2))]
# vv = [[0,0]*len(lst2)]
# print(v)
