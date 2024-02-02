from collections import deque


def isMaxList(lst, idx):
    tmpVal = lst[idx]
    tmp = lst[:idx] + lst[idx + 1:]
    tmp.sort()
    tmpQ = deque(tmp)

    valOne = 0
    valTwo = 0

    val = tmpQ.popleft()
    valOne = abs(sum(tmpQ) + tmpVal)

    tmpQ.appendleft(val)
    valT = tmpQ.pop()

    valTwo = abs(sum(tmpQ) + tmpVal)

    if valOne >= valTwo:
        return valOne
    else:
        return valTwo


def main():
    t = int(input())

    for k in range(1, t + 1):
        n = int(input())
        n_list = list(map(int, input().split()))
        sumVal = abs((sum(n_list) * n))
        removeVal = 0
        if n == 1:
            removeVal = n_list[0]
        else:
            for i in range(n):
                tmp = isMaxList(n_list, i)
                removeVal += tmp
        resultVal = max(removeVal, sumVal)
        print('#' + str(k),resultVal % 1000000007)


if __name__ == '__main__':
    main()