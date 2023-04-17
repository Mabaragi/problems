import sys
from collections import deque

K = int(sys.stdin.readline())
M, N = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = 10e8

visit = [[[INF] * (K + 1) for _ in range(M)] for _ in range(N)]

qu = deque([(0, 0, K)])
visit[0][0][K] = 0

while qu:
    ci, cj, ck = qu.popleft()
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M and visit[ni][nj][ck] > visit[ci][cj][ck] + 1 and array[ni][nj] == 0:
            visit[ni][nj][ck] = visit[ci][cj][ck] + 1
            qu.append((ni, nj, ck))
    for di, dj in ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1 , 2)):
        ni, nj, nk = ci + di, cj + dj, ck - 1
        if nk >= 0 and 0 <= ni < N and 0 <= nj < M and visit[ni][nj][nk] > visit[ci][cj][ck] + 1 and array[ni][nj] == 0:
            qu.append((ni, nj, nk))
            visit[ni][nj][nk] = visit[ci][cj][ck] + 1
            qu.append((ni, nj, nk))

ans = min(visit[N - 1][M - 1])
if ans == INF:
    print(-1)
else:
    print(ans)