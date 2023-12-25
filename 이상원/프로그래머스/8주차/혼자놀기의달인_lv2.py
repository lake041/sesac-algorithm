def solution(cards):
    anslst = []
    oc = [0 for i in range(len(cards))]
    cnt = 0
    for i in range(len(cards)):
        if oc[i] == 1:
            continue
        cnt+=1
        oc[i] = 1
        nextbox_num = cards[i]-1
        if oc[nextbox_num] ==0:
            while 1:
                oc[nextbox_num] =1
                nextbox_num = cards[nextbox_num]-1
                cnt+=1
                if oc[nextbox_num] == 1:
                    break
        
        anslst.append(cnt)
        cnt =0
    if len(anslst) ==1:
        return 0
    anslst.sort(reverse=True)

    return anslst[0]*anslst[1] 


print(solution([8,6,3,7,2,5,1,4]))