def solution(files):
    tmp = []
    head, number, tail = '', '', ''
    
    for file in files:       
        for i in range(len(file)):
            if file[i].isdigit():     # HEAD / NUMBER-TAIL 1차로 구분
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):    # NUMBER/ TAIL
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                tmp.append([head, number, tail])
                break

    
    # tmp = sorted(tmp, key=lambda x:(x[0].lower(), int(x[1]), x[2].lower()))
    tmp = sorted(tmp, key=lambda x:(x[0].lower(), int(x[1])))
    # 두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. 
    # MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다.
    # 위 조건 때문에 x[2]로는 정렬하지 않아야하는데 문제 잘못 읽어서 망함, 조심하자!
    

    return [''.join(i) for i in tmp]



print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]


print("01".isnumeric())
print(int("01"))



# 정규 표현식 풀이,,, 추후 공부해보기!
import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]