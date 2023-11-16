def solution(people, limit):
    answer = 0
    live = 0  # 구출된 사람 수

    rev_people = sorted(people, reverse=True)  # 몸무게 무거운 순
    people.sort()  # 몸무게 가벼운 순
    big = 0
    small = 0

    while (live < len(people)):
        if rev_people[big] + people[small] <= limit:
            live += 2
            answer, big, small = answer + 1, big + 1, small + 1
        else:
            live, answer, big = live + 1, answer + 1, big + 1

    return answer