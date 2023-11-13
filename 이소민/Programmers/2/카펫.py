def solution(brown, yellow):
    y_w, y_h = 0,0
    
    for i in range(brown):
        for j in range(0,i+1):
            y_w = i
            y_h = j
            if y_w*2 + y_h*2 + 4 == brown and y_w*y_h == yellow:
                return [y_w+2, y_h+2]