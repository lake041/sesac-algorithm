def solution(arrayA, arrayB):
    answer = 0

    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)

    if not canDivide(arrayB, gcdA):
        answer = gcdA

    if not canDivide(arrayA, gcdB):
        answer = max(answer, gcdB)

    return answer


from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def canDivide(array, a):
    return any(num % a == 0 for num in array)


