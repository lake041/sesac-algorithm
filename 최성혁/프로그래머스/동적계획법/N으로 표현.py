def solution(N, number):
    comb_list = [0, [N]]  # i번째 리스트는 N을 i개사용해서 나올 수 있는 숫자들의 리스트

    if N == number:  # N과 number가 같으면 그냥 N만 쓰면 되니 1이 된다.
        return 1

    for i in range(2, 9):  # 8개를 넘어서 쓰면 return -1이므로 8까지만 설정

        num_list = []  # N을 i개 사용해서 만들 수 있는 숫자 리스트

        dummy = int(str(N) * i)  # 사칙연산이 아닌 그냥 이어붙여서 나온 수 ex. 222 (N=2, i=3)
        comb_list.append(dummy)

        for k in range(1, i // 2 + 1):

            for x in comb_list[k]:
                for y in comb_list[x - k]:  # x와 y를 더하면 i 가 되도록 만든 수다.

                    # 덧셈
                    num_list.append(x + y)  # 각 사칙연산 결과를 더한다.

                    # 뺄셈
                    num_list.append(x - y)
                    num_list.append(y - x)

                    # 곱셈
                    num_list.append(x * y)

                    # 나눗셈
                    if x != 0:  # 나누기 위해 x는 0이 되어서는 안됨. 나머지는 무시하므로 // 사용
                        num_list.append(y // x)

                    if y != 0:
                        num_list.append(x // y)

            if number in num_list:  # 만약 i개를 사용해서 나올 수 있는 숫자 리스트 중 있다면 i를 return
                return i

            comb_list.append(num_list)  # 다음 i에서 이용해야하므로 리스트에 넣어둠

    return -1  # 8을 넘어가면 -1을 return