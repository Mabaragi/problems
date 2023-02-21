N, M = map(int, input().split())
maze = [[0] * (M + 2)] + [[0] + list(map(int, input())) + [0] for _ in range(N)] + [[0] * (M + 2)]

visit = [[0] * (M + 2) for _ in range(N + 2)]
q = [(1, 1)]
visit[1][1] = 1
while q:
    si, sj = q.pop(0)
    if (si, sj) == (N, M):
        break
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = si + di, sj + dj
        if visit[ni][nj] == 0 and maze[ni][nj] != 0:
            q.append((ni, nj))
            visit[ni][nj] = visit[si][sj] + 1
print(visit[N][M])