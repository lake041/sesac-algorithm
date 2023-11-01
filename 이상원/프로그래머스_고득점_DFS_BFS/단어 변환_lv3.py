from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0;
    visited = [False]*len(words)

    q = deque()
    q.append([begin, 0])
    while q:
        popword, step = q.popleft()
        if popword == target:
            answer=step
            return answer

        for i in range(len(words)):
            temp = 0
            if not visited[i]:
                for j in range(len(words[0])):
                    if popword[j] != words[i][j]:
                        temp += 1
                if temp == 1:
                        q.append([words[i], step+1])
                        visited[i] = True    
                
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))