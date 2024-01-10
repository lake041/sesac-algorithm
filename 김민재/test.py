from collections import deque
import sys
import heapq
input = sys.stdin.readline

def solve(p_list, n_list, ans, n_cnt):
    # 음수
    if (n_cnt % 2) != 0:
        ans += n_list.pop()
    while n_list:
        tmp = 0
        for i in range(2):
            if n_list:
                n_num = heapq.heappop(n_list)
                if tmp == 0:
                    tmp = n_num
                else:
                    tmp *= n_num
        ans += tmp

    while p_list:
        tmp = 0
        for i in range(2):
            if p_list:
                p_num = heapq.heappop(p_list)
                if tmp == 0:
                    tmp = p_num[1]
                else:
                    tmp *= p_num[1]
        ans += tmp

    return ans
def main():
    n = int(input())
    p_list = []
    n_list = []
    ans = 0
    n_cnt = 0
    for i in range(n):
        num = int(input())
        if num <= 0:
            heapq.heappush(n_list, num)
            n_cnt += 1
        elif num > 1:
            heapq.heappush(p_list, (-num, num))
        else:
            ans += num
    

    print(solve(p_list, n_list, ans, n_cnt))
    
if __name__ == "__main__":
    main()