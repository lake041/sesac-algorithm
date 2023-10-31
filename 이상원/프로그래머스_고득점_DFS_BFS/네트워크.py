from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)] 
    def bfs(pop):
        queue = deque()
        queue.append(pop)
        while queue:
            pop = queue.popleft()
            visited[pop] = 1
            for m in range(n):
                if computers[pop][m]==1 and visited[m] == 0:
                    queue.append(m)
    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            answer+=1
        

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


if 1:
    print("ooo")

if 0:
    print("ooooooooo")