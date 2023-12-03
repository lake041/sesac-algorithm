def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    # dic 이용
    phone_hash = {}

    for phone_number in phone_book:
        phone_hash[phone_number] = True

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in phone_hash and temp != phone_number:
                return False

    return True

solution(["12","123","1235","567","88"])