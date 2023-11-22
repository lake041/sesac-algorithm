def solution(arr):
    M, m = {}, {}
    nums = [int(x) for x in arr[::2]] # [1, 3, 5, 8]
    ops = [x for x in arr[1::2]] # ['-', '+', '-']
    
    for i in range(len(nums)):
        M[(i, i)] = nums[i] # {(0, 0): 1, (1, 1): 3, (2, 2): 5, (3, 3): 8}
        m[(i, i)] = nums[i] # {(0, 0): 1, (1, 1): 3, (2, 2): 5, (3, 3): 8}
    
    # i~j 까지 모든 경우의 수를 구함
    for d in range(1, len(nums)):
        # d = 1,2,3
        for i in range(len(nums)):
            # i = 0,1,2,3
            j = i + d 
            # j = 1,2,3,4/ 2,3,4,5/ 3,4,5,6
            if j >= len(nums):
                continue
                # j = 1,2,3, - / 2,3, -,-/ 3,-,-,-
            
            maxcandidates, mincandidates = [], []
            for k in range(i+1, j+1):
                # print("k = ", k)
                # print(i, k-1, "~", k, j)
                if ops[k-1] == '-':
                    mx = M[(i, k-1)] - m[(k, j)] # 최댓값을 위해서는 M[(i, k-1)] - m[(k, j)] 를 기억
                    mn = m[(i, k-1)] - M[(k, j)] # 최솟값을 위해서는 m[(i, k-1)] - M[(k, j)] 를 기억
                    maxcandidates.append(mx)
                    mincandidates.append(mn)
                else:
                    mx = M[(i, k-1)] + M[(k, j)] # 최댓값을 위해서는 M[(i, k-1)] + M[(k, j)] 를 기억
                    mn = m[(i, k-1)] + m[(k, j)] # 최솟값을 위해서는 m[(i, k-1)] + m[(k, j)] 를 기억
                    maxcandidates.append(mx)
                    mincandidates.append(mn)
                # print("max : ", maxcandidates)
                # print("min : ",mincandidates)

            M[(i, j)] = max(maxcandidates) # i~j까지 maxcandidates 중 가장 큰 값 저장
            m[(i, j)] = min(mincandidates) # i~j까지 mincandidates 중 가장 작은 값 저장
            # print(M)
            # print("=========================")
    return M[(0, len(nums) - 1)]