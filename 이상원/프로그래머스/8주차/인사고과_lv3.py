




def solution(scores):
    answer = 1
    wanho = scores[0]
    sum_wanho = wanho[0] + wanho[1]
    scores.sort(key=lambda x:(-x[0], x[1]))
    flag = 0
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        if flag <= score[1]:
            if sum_wanho < score[0] + score[1]:
                answer += 1
            flag = score[1]
    return answer

solution([[2,2],[1,4],[3,2],[3,2],[2,1]])
import heapq
def solution1(scores):
    answer = 0
    # scores.sort(reverse=True, key=lambda x:(x[0]+x[1]))

    # print(scores)
    lst = []
    for i in scores:
        heapq.heappush(lst,i)
    
    print(lst)
    return answer


solution([[2,2],[1,4],[3,2],[3,2],[2,1]])