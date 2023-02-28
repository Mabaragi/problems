N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(M):
        if array[i][j] == 2:
            virus.append((i, j))

ans = 0

for i in range(M * N - 2):
    if array[i // M][i % M] == 0:
        for j in range(i + 1, M * N - 1):
            if array[j // M][j % M] == 0:
                for k in range(j + 1, M * N):
                    if array[k // M][k % M] == 0:
                        array[i // M][i % M] = 1
                        array[j // M][j % M] = 1
                        array[k // M][k % M] = 1

                        visit = [[0] * (M + 1) for _ in range(N + 1)]
                        for v in virus:
                            q = [v]
                            ci, cj = v
                            visit[ci][cj] = 1
                            while q:
                                ci, cj = q.pop(0)
                                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                                    ni, nj = ci + di, cj + dj
                                    if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0 and array[ni][nj] != 1:
                                        visit[ni][nj] = 1
                                        q.append((ni, nj))
                        cnt = 0
                        for r in range(N):
                            for c in range(M):
                                if array[r][c] == 0 and visit[r][c] == 0:
                                    cnt += 1
                        array[i // M][i % M] = 0
                        array[j // M][j % M] = 0
                        array[k // M][k % M] = 0
                        if ans < cnt:
                            ans = cnt
print(ans)
