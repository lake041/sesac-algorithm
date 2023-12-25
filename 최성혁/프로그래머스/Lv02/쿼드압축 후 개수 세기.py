from collections import deque
def check_all_number(x,y,length,arr,check_num):
        for i in range(x,x+length):
            for j in range(y,y+length):
                if arr[i][j] != check_num:
                    return False
        return True
def solution(arr):
    answer = [0,0]
    queue = deque()
    queue.append((0,0,len(arr)))
    while queue:
        x,y,length = queue.popleft()
        check_num = arr[x][y]
        if check_all_number(x,y,length,arr,check_num):
            # 만약 모든 값이 같다면
            answer[check_num] +=1
        else: # 다른 값이 있다면
            # length //2 * 4번 반복
            split_len = length//2
            if split_len == 1:
                for i in range(x,x+length):
                    for j in range(y,y+length):
                        answer[arr[i][j]] +=1
            else:
                queue.append((x,y,split_len))
                queue.append((x+split_len,y,split_len))
                queue.append((x,y+split_len,split_len))
                queue.append((x+split_len,y+split_len,split_len))
    return answer