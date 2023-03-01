import sys
from collections import deque

def bfs(si, sj):
    qu = deque([(si, sj)])
    visit = [[0] * M for _ in range(N)]
    visit[si][sj] = 1
    while qu:
        ci, cj, = qu.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0 and array[ci][cj] == '0':
                visit[ni][nj] = visit[ci][cj] + 1
                qu.append((ni, nj))
    return visit


N, M = map(int, sys.stdin.readline().split())
array = [list(sys.stdin.readline()) for _ in range(N)]

array1 = bfs(0, 0)
array2 = bfs(N - 1, M - 1)
ans = 2 * N * M + 100
for i in range(N):
    for j in range(M):
        if array1[i][j] != 0 and array2[i][j] != 0 and array1[i][j] + array2[i][j] < ans:
            ans = array1[i][j] + array2[i][j] - 1
if ans == 2 * N * M + 100:
    print(-1)
else:
    print(ans)
