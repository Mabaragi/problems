from collections import defaultdict

def solution(genres, plays):
    N = len(genres)
    musics = []
    genre_play_times = defaultdict(int)
    for i in range(N):
        genre_play_times[genres[i]] += plays[i]
        musics.append((i, genres[i], plays[i]))
    musics.sort(key=lambda x: (genre_play_times[x[1]] * -1, x[2] * -1))
    
    answer = []
    genre_numbers = defaultdict(int)
    for music in musics:
        if genre_numbers[music[1]] < 2:
            genre_numbers[music[1]] += 1
            answer.append(music[0])
    return answer