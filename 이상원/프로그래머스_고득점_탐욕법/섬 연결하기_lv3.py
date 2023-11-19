def solution(n, costs):
    answer = 0
    node = [0]
    while 1:
        candidate = []
        for j in node:
            for i in costs:
                if i[0] == j:
                    candidate.append(i) # 후보를 뽑아
        if not candidate:
            return answer

        mcic = candidate[0][2] #min_cost_in_candidate
        mcic_i = 0 
        for i, cand in enumerate(candidate):
            if (mcic > cand[2]): #후보중에 가장 싼곳 선택 근데 첫번쨰로 싼곳이 선택되긴함,,ㅠ
                mcic = cand[2]
                mcic_i = i
            
        node.append(candidate[mcic_i][1]) # 노드에 방문한 섬을 넣어
        answer += candidate[mcic_i][2]  # 방문하기위해 다리지은 비용을 엔서에 추가해
        costs.remove(candidate[mcic_i]) # 지불한 비용은 코스트에서 빼
        if (len(node) == n):
            break
    return answer

def solution(n, costs):
    answer = 0
    node = [0]
    a = fs(node, costs, answer,n)
    return  a


def fs(node, costs, answer,n):
    if not costs or len(node) ==n:
        return [answer]
    
    candidate = []
    for j in node:
        for i in costs:
            if i[0] == j:
                candidate.append(i) # 후보를 뽑아

    mcic = candidate[0][2] #min_cost_in_candidate
    mcic_i = 0 
    for i, cand in enumerate(candidate):
        if (mcic >= cand[2]): #후보중에 가장 싼곳 선택 근데 첫번쨰로 싼곳이 선택되긴함,,ㅠ
            node.append(cand[1])
            answer += cand[2]
            costs.remove(cand)
            answer = fs(node, candidate,answer,n)
    
    return answer
                


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) #4


# lst = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# lst.remove([0,1,1])
# print(lst)


# for i in []:
#     print(i)