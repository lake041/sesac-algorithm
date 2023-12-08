def solution(players, callings):
    answer = []
    temp = ""
    dic={}

    for i in range(len(callings)):
        if callings[i] in dic.keys():
            dic[callings[i]] += 1
        else:
            dic[callings[i]] = 1
    
    while 1:
        for i in dic.keys():
            temp_i = players.index(i)
            first = temp_i-dic[i]
            if first >= 0:
                temp_l = [i] + players[first:temp_i]
                for j in range(len(temp_l)):
                    players[first+j] = temp_l[j]
                dic[i] = 0    
            else:
                temp_l = [i] + players[0:temp_i]
                for j in range(len(temp_l)):
                    players[0+j] = temp_l[j]
                dic[i] += first
        if len(set(dic.values())) ==1:
            return players    
    
        
    return players

lst = ["mumu", "soe", "poe", "kai", "mine"]
lst2 = ["kai", "kai", "mine", "mine"]

lst2 = ["soe", "poe", "poe", "soe"]
print(lst[-1:0])
print(solution(lst, lst2))