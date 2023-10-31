def solution(nums):
    # 최대 N/2마리
    answer = set(nums)
    an = len(answer)
    N = len(nums) // 2
    if an > N:
        return N
    else:
        return an