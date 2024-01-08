from collections import defaultdict


def solution(tickets):
    answer = []
    graph = defaultdict(list)

    # 그래프 생성
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    # 알파벳 역순으로 정렬
    for key in graph:
        graph[key].sort(reverse=True)

    stack = ["ICN"]

    while stack:
        current = stack[-1]

        # 현재 위치에서 갈 수 있는 곳이 있다면
        if current in graph and graph[current]:
            stack.append(graph[current].pop())
        else:
            # 갈 수 있는 곳이 없으면 경로에 추가
            answer.append(stack.pop())

    # 경로를 역순으로 반환
    return answer[::-1]
