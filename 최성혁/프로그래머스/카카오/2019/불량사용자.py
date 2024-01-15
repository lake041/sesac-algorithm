'''
0. user_id의 모든 조합을 찾아낸 후
1. 각 조합과 banned_id의 조합이 일치하는 Check 함수를 이용하여
2. 맞으면 해당 조합을 tmp 리스트에 삽입
3. tmp 리스트의 길이를 리턴하면 끝
'''

from itertools import permutations

def check(user,banned_id):
    for i in range(len(banned_id)):
        if len(user[i]) != len(banned_id[i]):
            return False

        for j in range(len(user[i])):
            if user[i][j] == banned_id[i][j] or banned_id[i][j] == "*":
                continue
            else:
                return False
    return True


def solution(user_id, banned_id):
    user_list = list(permutations(user_id,len(banned_id)))
    resultList = []
    for user in user_list:
        if check(user,banned_id):
            if set(user) not in resultList:
                resultList.append(set(user))
    print(resultList)
    return len(resultList)

