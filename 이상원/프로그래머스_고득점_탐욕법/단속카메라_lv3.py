def solution(routes):
    routes.sort()
    ans_lst = [routes.pop(0)]
    while routes:
        pop = routes.pop(0)

        for i, ans in enumerate(ans_lst):
            if (ans[0] <= pop[0] and pop[0] <= ans[1]) or (ans[0] <= pop[1] and pop[1] <= ans[1]):
                lst = [ans[0],pop[0],ans[1], pop[1]]
                lst.sort()
                lst.pop(0)
                lst.pop()
                ans_lst[i] = lst
                break
            if i+1 == len(ans_lst):
                ans_lst.append(pop)
            


    return len(ans_lst)

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))