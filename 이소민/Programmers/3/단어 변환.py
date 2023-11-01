from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def can_change(word, change):
        diff = 0
        for i in range(len(begin)):
            if word[i] != change[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False
    q = deque()
    q.append((begin, 0))
    while q:
        word, depth = q.popleft()
        for i in words:
            if can_change(word, i):
                if i == target:
                    depth += 1
                    return depth
                else:
                    q.append((i, depth+1))