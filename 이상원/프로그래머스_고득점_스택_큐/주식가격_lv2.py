# def solution(prices):
#     answer = [0]*len(prices)
#     count = 0
#     for i in range(len(prices)):
#         count = 0
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 count+=1
#             else:
#                 count+=1
#                 break
#         answer[i] = count

            
#     return answer


# print(solution([1, 2, 3, 2, 3]))


def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            temp = stack.pop()
            answer[temp] = i-temp
        stack.append(i)

    while stack:
        temp = stack.pop()
        answer[temp] = len(prices)-1-temp 
    return answer
print(solution([1, 2, 3, 2, 3]))

