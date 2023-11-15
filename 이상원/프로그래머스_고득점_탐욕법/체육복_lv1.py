def solution(n, lost, reserve): 
    cnt = 0
    tmp = [i for i in lost if i in reserve] # 여벌있는데 도둑 맞은 사람
    for i in tmp:
        if i in lost:
            lost.remove(i)

    for i in tmp:
        if i in reserve:
            reserve.remove(i)

    answer = n - len(lost)

    lost.sort()
    reserve.sort()
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
            cnt+=1
            continue
        elif i+1 in lost:
            lost.remove(i+1)
            cnt+=1

    answer += cnt

    return answer

sol = solution(3,[3,1,2],[1,2])
print(sol)
def solution1(n, lost, reserve):
    answer = 0
    num_suit = []

    for i in range(n):
        num_suit.append(1)
        if i+1 in lost:
            num_suit[i] = num_suit[i]-1
        if i+1 in reserve:
            num_suit[i] = num_suit[i]+1
        
        
        # if i+1 in lost and i+1 in reserve:
        #     num_suit.append(0)
        # elif i+1 in reserve:
        #     num_suit.append(2)
        # elif i+1 in reserve:
        #     num_suit.append(1)
        # else:
        #     num_suit.append(1)

    # print(num_suit)
    num_suit.insert(0,9)
    num_suit.append(99)


    for i in range(len(num_suit)):
        if num_suit[i] == 99:
            break
        if num_suit[i]==0 and num_suit[i+1] ==2:
            num_suit[i]=1
            num_suit[i+1]=1
        if num_suit[i]==0 and num_suit[i-1]==2:
            num_suit[i]=1
            num_suit[i-1]=1
    
    answer = n-num_suit.count(0)
    # print(num_suit)
    return answer