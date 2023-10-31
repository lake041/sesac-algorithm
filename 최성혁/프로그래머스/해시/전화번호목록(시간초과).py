# 시간 초과 풀이
# 91.7 / 100
def solution(phone_book):
    # - slicing 길이만큼 & 정렬

    phone_book = sorted(phone_book, key=len)

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            l = len(phone_book[i])
            if phone_book[i] == phone_book[j][:l]:
                return False

    return True