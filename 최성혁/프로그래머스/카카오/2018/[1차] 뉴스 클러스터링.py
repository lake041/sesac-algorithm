from collections import deque
import math


def solution(str1, str2):
    a = []
    b = []

    # 다중집합 만들기 str1
    for i in range(1, len(str1)):
        tmp = str1[i - 1] + str1[i]
        for i in tmp:
            # 특수문자,공백등 제외
            if (ord(i) >= 32 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or ord(i) >= 123:
                break
        else:
            # 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다
            a.append(tmp.lower())
    # 다중집합 만들기(특수문자,공백등 제외) - str2
    for i in range(1, len(str2)):
        tmp = str2[i - 1] + str2[i]
        for i in tmp:
            # 특수문자,공백등 제외
            if (ord(i) >= 32 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or ord(i) >= 123:
                break
        else:
            # 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다
            b.append(tmp.lower())

    a.sort()
    b.sort()

    a = deque(a)
    b = deque(b)

    # 교집합
    inner = []
    # 합집합
    plus = []

    # 길이가 더 긴 리스트 기준
    if len(a) >= len(b):
        while a:
            # 처음 값 pop
            valA = a.popleft()
            for i in range(len(b)):
                # pop된값과 b의 원소 비교
                if b[i] == valA:
                    # 교집합에 넣어주고
                    inner.append(valA)
                    # b리스트 제거
                    b.remove(b[i])
                    break
            else:
                # 교집합에 안들어간다면 합집합에 넣어줌
                plus.append(valA)
        # 교집합에 남은 값들 넣어줌
        for i in inner:
            plus.append(i)
        while b:
            plus.append(b.popleft())
    else:
        while b:
            valB = b.popleft()
            for i in range(len(a)):
                if a[i] == valB:
                    inner.append(valB)
                    a.remove(a[i])
                    break
            else:
                plus.append(valB)

        for i in inner:
            plus.append(i)
        while a:
            plus.append(a.popleft())

    # 공집합이면 JaK = 1
    if len(inner) == 0 and len(plus) == 0:
        return 65536

    Jak = len(inner) / len(plus)

    answer = math.trunc(Jak * 65536)
    return answer