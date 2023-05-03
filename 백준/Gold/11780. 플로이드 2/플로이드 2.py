import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

INF = 1e11
d = [[INF] * (N + 1) for _ in range(N + 1)]
ans = [[[i] for _ in range(N + 1)] for i in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if d[a][b] > c:
        d[a][b] = c
        ans[a][b] = [b]
    # d[b][a] = min(d[b][a], c)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        ans[i][j] = [i] + ans[i][j]

for m in range(1, N + 1):
    for s in range(1, N + 1):
        if s == m: continue
        for e in range(1, N + 1):
            if s == e or e == m: continue
            if d[s][e] > d[s][m] + d[m][e]:
                d[s][e] = d[s][m] + d[m][e]
                ans[s][e] = ans[s][m] + ans[m][e][1:]


for i in range(1, N + 1):
    for j in range(1, N + 1):
        if d[i][j] == INF:
            d[i][j] = 0

for i in range(1, N + 1):
    print(*d[i][1:])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if d[i][j] == 0:
            print(0)
        else:
            print(len(ans[i][j]), *ans[i][j])