N, L, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:  # 인구 이동이 없을 때 까지 반복. k 는 연합의 개수. 연합의 개수가 N * N 이면 종료
    k = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                sm = 0
                qu = [(i, j)]
                lst = [[i, j]]
                visit[i][j] = 1
                while qu:
                    ci, cj = qu.pop(0)
                    sm += array[ci][cj]
                    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and L <= abs(
                                array[ci][cj] - array[ni][nj]) <= R:
                            qu.append((ni, nj))
                            visit[ni][nj] = 1
                            lst.append([ni, nj])
                k += 1  # 이전에 방문한 적이 없으면 연합
                n = len(lst)
                for r, c in lst:
                    array[r][c] = sm // n

    if k == N * N:
        break
    cnt += 1
print(cnt)