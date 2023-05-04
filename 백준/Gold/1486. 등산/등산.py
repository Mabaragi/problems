from collections import deque


def to_num(ch):
    if ch.isupper():
        return ord(ch) - ord('A')
    else:
        return ord(ch) - ord('a') + 26


def get_max():
    mx = 0
    for i in range(N):
        for j in range(M):
            if visit_to[i][j] + visit_from[i][j] <= D and mx < array[i][j]:
                mx = array[i][j]
    return mx


def bfs(drc):
    visit = [[1e8] * M for _ in range(N)]
    visit[0][0] = 0
    qu = deque([(0, 0)])
    while qu:
        ci, cj = qu.popleft()
        if visit[ci][cj] > D:
            continue
        if drc == 1 and visit_to[ci][cj] + visit[ci][cj] > D:
            continue
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, - 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and abs(array[ni][nj] - array[ci][cj]) <= T:
                if array[ni][nj] * drc < array[ci][cj] * drc and visit[ni][nj] > visit[ci][cj] + abs(
                        array[ni][nj] - array[ci][cj]) ** 2:
                    visit[ni][nj] = visit[ci][cj] + abs(array[ni][nj] - array[ci][cj]) ** 2
                    qu.append((ni, nj))
                elif array[ni][nj] * drc >= array[ci][cj] * drc and visit[ni][nj] > visit[ci][cj] + 1:
                    visit[ni][nj] = visit[ci][cj] + 1
                    qu.append((ni, nj))
    return visit


N, M, T, D = map(int, input().split())
array = [list(map(to_num, input())) for _ in range(N)]
visit_to = bfs(-1)
visit_from = bfs(1)
print(get_max())