def solution(answers):
    answer = []
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [[1,0],[2,0],[3,0]]
    for i in range(len(answers)):
        if answers[i] == ans1[i%len(ans1)]:
            cnt[0][1] +=1
        if answers[i] == ans2[i%len(ans2)]:
            cnt[1][1] +=1
        if answers[i] == ans3[i%len(ans3)]:
            cnt[2][1] +=1

    cnt.sort(key=lambda x: (-x[1], x[0]))

    print(cnt)

solution([1,2,3,4,5])     

def solution(answers):
    
    answer = []
    score = [0,0,0]
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)) :
        if answers[i] == student1[i%5] :
            score[0] += 1
        if answers[i] == student2[i%8] :
            score[1] += 1
        if answers[i] == student3[i%10] :
            score[2] += 1
        
    for idx, num in enumerate(score) :
        if num == max(score) :
            answer.append(idx +1)
    
    return answer