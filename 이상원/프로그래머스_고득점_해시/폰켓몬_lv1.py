def solution(nums):
    answer = 0
    nums_set = set(nums) 
    nums_list = list(nums_set) 
    if len(nums_list)>=(len(nums)/2):
        answer = len(nums)/2
    else:
        answer = len(nums_list)
    
    return answer