def solution(N, number):
    if number == 1:
        return 1
    set_list = []

    for cnt in range(1, 9): # 1~8
        partial_set = set()
        partial_set.add(int(str(N) * cnt)) # 이어 붙여서 만드는 경우 넣기
        for i in range(cnt - 1): # (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for j in set_list[i]:
                for k in set_list[-i - 1]:
                    partial_set.add(j + k)
                    partial_set.add(j * k)
                    partial_set.add(j - k)
                    if k != 0:
                        partial_set.add(j / k)
        # 만든 집합에 number가 처음 나오는지 확인
        if number in partial_set:
            return cnt
        set_list.append(partial_set)
    return -1



partial_set = set()

partial_set.add(5)
partial_set.add(5)
print(partial_set)
print(solution(5,12))


print(solution(2,11))