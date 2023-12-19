from math import gcd
def solution(arrayA, arrayB):
    a = arrayA[0]
    b = arrayB[0]
    for i in range(len(arrayA)):
        a = gcd(a, arrayA[i])
        b = gcd(b, arrayB[i])

    x = 1
    y = 1
    for i in range(len(arrayA)):
        if arrayA[i] % b == 0:
            x = 0
        if arrayB[i] % a == 0:
            y = 0
    if x == 0 and y == 0:
        return x
    else:
        return max(a, b)
