# 복습 필요
def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(al):
        if ord(al) > 78:
            return 90-ord(al)+1
        else:
            return ord(al)-65

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer

from collections import deque

def solution(name):
    # 검수 여부 체크
    is_checked = [False for _ in range(len(name))]
    # A 를 true로
    for i in range(len(name)):
        if name[i] == 'A':
            is_checked[i] = True
    q = deque([])
    q.append((0, is_checked, 0))
    
    # 전체가 다 A면 볼 필요가 없어서 0을 return
    if name.count('A') == len(name):
        return 0
    
    while q:
        # 현재 검사하는 idx, 현재 체크 여부, 현재까지의 답
        idx, each_checked, ans = q.popleft()
        # 만약 체크 안 된 곳이면
        if not each_checked[idx]:
            each_checked[idx] = True # 체크 처리
            ans += min((ord(name[idx]) - ord('A')), (ord('Z') - ord(name[idx]) + 1))
        # 모두 검사가 됐으면 ans 반환
        if all(each_checked):
            return ans
        else:
            # 앞 뒤 인덱스를 q에 넣어줌
            q.append((idx + 1, each_checked.copy(), ans + 1))
            q.append((idx - 1, each_checked.copy(), ans + 1))
        
    return ans