from collections import Counter, defaultdict


def solution(genres, plays):
    # 정답
    answer = []

    # 장르별 리스트
    dic = defaultdict(list)

    # 장르별 재생횟수 총합
    g = Counter()

    for idx, play in enumerate(plays):
        # 장르명
        tmp = genres[idx]

        dic[tmp].append((idx, play))
        g[tmp] += play

        # 재생횟수별 정렬
        g = g.most_common()

        for i, j in g:

            tmp_list = dic[i]

            if len(tmp_list) >= 2:
                # 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
                # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
                tmp_list.sort(key=lambda x: x[0])
                tmp_list.sort(key=lambda x: x[1], reverse=True)
                for k in range(2):
                    answer.append(tmp_list[k][0])
            else:
                answer.append(tmp_list[0][0])

        return answer