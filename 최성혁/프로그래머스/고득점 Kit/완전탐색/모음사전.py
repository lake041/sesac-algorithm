def solution(word):
    alphabet = {0:'A', 1:'E', 2:'I', 3:'O', 4:'U'}
    rev_alphabet = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    cnt = 0
    string = []
    while True:
        cnt += 1
        # 문자열의 개수가 5 미만일 경우, 뒤에 문자를 추가해줌
        if len(string) < 5:
            string.append('A')
        # 맨 뒤 문자가 'U'일 경우, 문자열 표현의 한계에 다다랐으므로 앞의 문자를 한 수준 증가함
        elif string[-1] == 'U':
            while string[-1] == 'U':
                string.pop()
            string[-1] = alphabet[rev_alphabet[string[-1]] + 1]
        else:
            string[-1] = alphabet[rev_alphabet[string[-1]] + 1]
        if string == list(word):
            return cnt