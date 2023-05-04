from collections import deque


to_num = lambda ch: ord(ch) - ord('A') if ch.isupper() else ord(ch) - ord('a') + 26


def get_max():
    return max([array[i][j] for i in range(N) for j in range(M) if visit_to[i][j] + visit_from[i][j] <= D])


def bfs(drc):
    visit = [[1e8] * M for _ in range(N)]
    visit[0][0] = 0
    qu = deque([(0, 0)])
    while qu:
        ci, cj = qu.popleft()
        if drc == 1 and visit_to[ci][cj] + visit[ci][cj] > D:
            continue
        if visit[ci][cj] > D:
            continue
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and abs(array[ni][nj] - array[ci][cj]) <= T:
                cost = (array[ni][nj] - array[ci][cj]) ** 2 if array[ni][nj] * drc < array[ci][cj] * drc else 1
                if visit[ni][nj] > visit[ci][cj] + cost:
                    visit[ni][nj] = visit[ci][cj] + cost
                    qu.append((ni, nj))
    return visit


N, M, T, D = map(int, input().split())
array = [list(map(to_num, input())) for _ in range(N)]
visit_to = bfs(-1)
visit_from = bfs(1)
print(get_max())