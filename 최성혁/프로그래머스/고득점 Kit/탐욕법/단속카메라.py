def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    cam = routes[0][1]
    for idx in range(1, len(routes)):
        if (routes[idx][0] > cam):
            cam = routes[idx][1]
            answer += 1

    return answer