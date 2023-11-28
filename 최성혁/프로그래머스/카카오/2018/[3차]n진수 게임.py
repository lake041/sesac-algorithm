def convert(number, n):
    if number == 0:
        return '0'
    numbers = "0123456789ABCDEF"
    res = ""
    while number > 0:
        number, mod = divmod(number, n)
        res += numbers[mod]
    return res[::-1]

def solution(n, t, m, p):
    answer = ''
    game = ''.join(convert(num, n) for num in range(t * m))
    answer = game[p-1::m][:t]
    return answer

