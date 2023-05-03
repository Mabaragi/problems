import sys

N, M = map(int, sys.stdin.readline().split())
INF = 10e6
d = [[INF] * (N + 1) for _ in range(N + 1)]
ans = [['-' for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    d[a][b] = c
    d[b][a] = c
    # ans[a][b].append(b + 1)
    # ans[b][a].append(a + 1)
    ans[a][b] = b
    ans[b][a] = a

for m in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            if d[s][e] > d[s][m] + d[m][e] and s != e:
                d[s][e] = d[s][m] + d[m][e]
                ans[s][e] = ans[s][m]

for i in range(1, N + 1):
    print(*ans[i][1:])
