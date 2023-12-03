def solution(array, commands):
    # commands의 [i,j,k]를 뽑아
    answer = []
    for i in range(len(commands)):
        tempArray = []
        firstIndex = commands[i][0]
        lastIndex = commands[i][1]
        targetIndex = commands[i][2]
        tempArray = array[firstIndex - 1:lastIndex]
        tempArray.sort()
        answer.append(tempArray[targetIndex - 1])

    return answer