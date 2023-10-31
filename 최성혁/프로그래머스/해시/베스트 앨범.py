from collections import defaultdict

def solution(genres, plays):
    genre_play_count = defaultdict(int)
    song_info = defaultdict(list)

    # 각 장르의 전체 재생 횟수 계산
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        # 각 노래의 정보(인덱스, 재생 횟수) 저장
        song_info[genre].append((i, play))

    # 장르별 총 재생 횟수를 기준으로 내림차순으로 정렬
    sorted_genres = sorted(genre_play_count, key=lambda x: genre_play_count[x], reverse=True)

    answer = []
    for genre in sorted_genres:
        # 각 장르 안에서 노래들의 재생 횟수를 기준으로 내림차순, 인덱스가 작은 순서로 정렬
        song_info[genre].sort(key=lambda x: (-x[1], x[0]))

        # 장르 내에서 최대 2곡까지만 선택
        for i in range(min(2, len(song_info[genre]))):
            answer.append(song_info[genre][i][0])

    return answer
