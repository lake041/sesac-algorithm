# from itertools import product, permutations, combinations
# def solution(number, k):
#     len_ans = len(number)-k
#     answer = "1"
#     first = 0
#     sec = 0
#     ans = ""
#     while 1:
        
#         for i in range(len(number)):
            
#             if (len_ans==len(number)-i):
#                 break
#             if answer < number[i]:
#                 answer = number[i]
#                 first = i+1
            
#         number = number[first:]
#         ans += answer
#         if len(number) == len_ans- len(ans):
#             ans += number
#         else:
#             len_ans = len_ans- len(ans)
#         answer="1"
#         # 3234
#         if len(ans) == len_ans:
#             break

#     return ans


# def solution(number, k):
#     answer = [] # Stack
    
#     for num in number:
#         if not answer:
#             answer.append(num)
#             continue
#         if k > 0:
#             while answer[-1] < num:
#                 answer.pop()
#                 k -= 1
#                 if not answer or k <= 0:
#                     break
#         answer.append(num)
        
#     answer = answer[:-k] if k > 0 else answer
#     return ''.join(answer)
# number = "1231234"
    # while 1:
    #     grdval = "0"

    #     for i in range(first, len(number)):
            
    #         if (i>len_ans):
    #             sec=i
    #             break
    #         answer += max(answer, number[i])

    #     for i in range(sec, len(number)):        

    # print(answer)
     

# number = "12312343333"

    # k = len(number)-k
    # number = [[j,i] for i,j in enumerate(number)]
    
    # enum = list(permutations(number,k))
    # maxnum = 0
    # for i in enum:
    #     snum = ""
    #     for j in i:
    #         snum += j[0]
    #         tmp = int(snum)
    #         maxnum = max(maxnum, tmp) 
   

# number= "1924"
# number = "1231234"
# # print(len(number))
# # number = [[j,i] for i,j in enumerate(number)]
# print(solution(number, 3))

# a= [[1,0],[5,1],[4,2],[9,3],[5,4]]
# print(list(permutations(a,2)))
# print(list(product(a, repeat=2)))



def solution(number, k):
    # return max(["".join(i) for i in list(combinations(number,len(number)-k))])
    lst = list(number)
    
    answer = ""
    remain_len = len(lst)- k
    i, j = 0, 0 - remain_len + 1
    while 1:
        # print(lst[i:j])
        if j == 0:
            j = len(number)
        if lst[i:j]:
            answer += max(lst[i:j])
        else:
            return answer
        remain_len -= 1
        if len(answer) == len(number) - k:
            return answer
        i += lst[i:j].index(answer[-1])+1
        j = 0 - remain_len + 1
        


# print(solution("4177252841",4))
print(solution("6547", 3))

# print("4177252841"[8:10])