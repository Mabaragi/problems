from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

"""
box는 3차원 배열. [z][y][x]  z = 높이, y = 세로, x= 가로
"""
visit = [[0] * M for _ in range(N)]
q = deque([])
cnt = 0
# 익은 토마토의 위치를 큐 리스트에 저장 cnt는 토마토가 익는지 판별용.

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
            visit[i][j] = 1
            cnt += 1
        elif box[i][j] == -1:
            cnt += 1
while q:
    si, sj = q.popleft()
    for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M and box[ni][nj] == 0:
            q.append((ni, nj))
            visit[ni][nj] = visit[si][sj] + 1
            box[ni][nj] = 1
            cnt += 1
if cnt == M * N:
    print(visit[si][sj] - 1)
else:
    print('-1')
