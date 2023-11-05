from collections import deque

def solution(begin,target,words):
    if target not in words:
        return 0
    return bfs(begin,target,words)


def bfs(begin,target,words):
    queue = deque()
    queue.append([begin,0])
    while queue:
        root,count = queue.popleft()

        if root == target:
            return count

        for word in words:
            cnt = 0
            for i in range(len(root)):
                if root[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                queue.append([word,count + 1])
