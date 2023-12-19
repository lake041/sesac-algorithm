def solution(s):
    answer = ''
    s = s.title()

    arr = list(s.split(' '))
    for idx, word in enumerate(arr):
        try:
            int(word[0])
            word = word[0] + word[1].lower() + word[2:]
            del arr[idx]
            arr.insert(idx, word)
        except:
            continue

    answer = ' '.join(arr)
    return answer