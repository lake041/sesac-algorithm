from collections import deque
import math
def solution(n, words):
    answer = []
    # 탈락하는 사람 없으면 [0,0]
    # 첫 탈락자의 번호 n과 몇 번 순환째에 탈락하는지 m [n,m]
    m = 1
    q = deque(words[1:])
    past = [words[0]]
    
    while q:
        word = q.popleft()
        m +=1
        if word not in past and word[0] == past[-1][-1]:
            past.append(word)
        else:
            break
    
    if m == len(words) and len(past) == len(words):
        answer = [0,0]
    else:
        fir = m%n
        if fir ==0:
            fir = n
        answer = [fir , math.ceil(m/n)]
    return answer