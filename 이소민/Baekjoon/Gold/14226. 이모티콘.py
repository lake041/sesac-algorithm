from collections import deque
from copy import deepcopy
s = int(input())
q = deque()
# 클립보드, 이모지, 시간
q.append((0, 1 ,0))

visited = [[False] * 1001 for _ in range(1001)]
visited[0][1] = True

while q:
    clipboard, emoji, time = q.popleft()
    if emoji == s:
        print(time)
        exit()
    for i in range(3):
        if i == 0:
            # 화면에 있는 이모티콘을 클립보드에 복사
            tmp_clipboard = emoji
            tmp_emoji = emoji
        elif i == 1 and clipboard!= 0:
            # 클립보드에 있는 모든 이모티콘 화면에 붙어넣기
            tmp_clipboard = clipboard
            tmp_emoji = emoji+clipboard
        elif i == 2 and emoji!=0:
            # 화면에 있는 이모티콘 중 하나 제거
            tmp_clipboard = clipboard
            tmp_emoji = emoji-1
        if tmp_emoji >= 1001 or tmp_emoji < 0 or tmp_clipboard >= 1001 or tmp_clipboard < 0 or visited[tmp_clipboard][
            tmp_emoji]:
            continue
        # 방문처리 후 연산 횟수를 +1 하여 큐에 추가
        visited[tmp_clipboard][tmp_emoji] = True
        q.append([tmp_clipboard, tmp_emoji, time + 1])