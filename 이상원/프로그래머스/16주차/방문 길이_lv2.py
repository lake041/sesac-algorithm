from collections import deque

def solution(dirs):
    answer = 0
    q = deque(list(dirs))
    bod = [[[] for _ in range(11)] for _ in range(11)]
    # bod[5][5] = [dirs[0]]

    x,y= 5,5

    while q:
        inc = q.popleft()
        
        if inc == "L":
            dx, dy = x,y-1
            if 0<=dx<11 and 0<=dy<11:
                if "R" not in bod[dx][dy]:
                    bod[dx][dy].append("R")
                    bod[x][y].append("L")
                    answer+=1
                x,y = dx,dy
        elif inc == "R":
            dx, dy = x,y+1
            if 0<=dx<11 and 0<=dy<11:
                if "L" not in bod[dx][dy]:
                    bod[dx][dy].append("L")
                    bod[x][y].append("R")
                    answer+=1
                x,y = dx,dy
        elif inc == "U":
            dx, dy = x-1,y
            if 0<=dx<11 and 0<=dy<11:
                if "D" not in bod[dx][dy]:
                    bod[dx][dy].append("D")
                    bod[x][y].append("U")
                    answer+=1
                x,y = dx,dy
        elif inc == "D":
            dx, dy = x+1,y
            if 0<=dx<11 and 0<=dy<11:
                if "U" not in bod[dx][dy]:
                    bod[dx][dy].append("U")
                    bod[x][y].append("D")
                    answer+=1
                x,y = dx,dy

            
    return answer


print(solution("ULURRDLLU"))