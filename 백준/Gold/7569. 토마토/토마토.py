
from collections import deque

M, N, H = map(int, input().split())
box = []
for i in range(H):
    box.append([list(map(int, input().split())) for _ in range(N)])

"""
box는 3차원 배열. [z][y][x]  z = 높이, y = 세로, x= 가로
"""
visit = [[[0] * M for _ in range(N)] for _ in range(H)]
q = deque([])
cnt = 0
# 익은 토마토의 위치를 큐 리스트에 저장 cnt는 토마토가 익는지 판별용.
for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 1:
                q.append((k, i, j))
                visit[k][i][j] = 1
                cnt += 1
            elif box[k][i][j] == -1:
                cnt += 1
while q:
    sk, si, sj = q.popleft()
    for dk, di, dj in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)):
        nk, ni, nj = sk + dk, si + di, sj + dj
        if 0 <= nk < H and 0 <= ni < N and 0 <= nj < M and box[nk][ni][nj] == 0:
            q.append((nk, ni, nj))
            visit[nk][ni][nj] = visit[sk][si][sj] + 1
            box[nk][ni][nj] = 1
            cnt += 1
if cnt == M * H * N:
    print(visit[sk][si][sj] - 1)
else:
    print('-1')