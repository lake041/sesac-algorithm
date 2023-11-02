def solution(genres, plays):
    answer = [] 

    dic_genre = {}
    for i in range(len(genres)):
        if genres[i] not in dic_genre.keys():
            dic_genre[genres[i]] = plays[i]
        else:
            dic_genre[genres[i]] += plays[i]


    sorted_dict = dict(sorted(dic_genre.items(), key= lambda item:-item[1]))
    # print(sorted_dict)
    
    for key in sorted_dict.keys():
        a ={}
        for i in range (len(plays)):        
            if genres[i] == key:    
                a[i] = plays[i]
        sorted_a = dict(sorted(a.items(), key= lambda item:-item[1]))
        print(sorted_a)
        for i in range(len(sorted_a.keys())):
            if i >1:
                break
            answer.append(list(sorted_a.keys())[i])

    return answer



a = ["classic", "pop", "classic", "classic", "pop"]	
b = [500, 600, 150, 800, 2500]

print(solution(a,b))