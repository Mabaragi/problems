import sys
from collections import defaultdict

N = int(sys.stdin.readline())
balls = sorted([[tuple(map(int, sys.stdin.readline().split())), i] for i in range(N)], key=lambda x:(x[0][1], x[0][0]))
color_score = defaultdict(int)
weight_score = defaultdict(int)
color_score[balls[0][0][0]] = balls[0][0][1]
weight_score[balls[0][0][1]] = balls[0][0][1]
score = [0] * N
accum_score = [0] * N
accum_score[0] = balls[0][0][1]
for i in range(1, N):
    accum_score[i] = accum_score[i - 1] + balls[i][0][1]
for i in range(1, N):
    (ball_color, ball_score), ball_number = balls[i]
    if balls[i][0] == balls[i - 1][0]:
        score[ball_number] = score[balls[i-1][1]]
    else:
        score[ball_number] = accum_score[i - 1] - weight_score[ball_score] - color_score[ball_color]
    color_score[ball_color] += ball_score
    weight_score[ball_score] += ball_score

for i in score:
    print(i)