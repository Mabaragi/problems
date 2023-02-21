N = int(input())
houses = [[0] * (N + 2)] + [[0] + list(map(int, input())) + [0] for _ in range(N)] + [[0] * (N + 2)]

visit = [[0] * (N + 2) for _ in range(N + 2)]
ans = []
ans2 = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if houses[i][j] == 1 and visit[i][j] == 0:
            ans2 += 1
            stk = []
            si, sj = i, j
            visit[si][sj] = 1
            cnt = 1
            while True:
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni, nj = si + di, sj + dj
                    if houses[ni][nj] == 1 and visit[ni][nj] == 0:
                        stk.append((si, sj))
                        si, sj = ni, nj
                        visit[si][sj] = 1
                        cnt += 1
                        break
                else:
                    if stk:
                        si, sj = stk.pop()
                    else:
                        ans.append(cnt)
                        break
ans.sort()
print(ans2)
print(*ans, sep='\n')