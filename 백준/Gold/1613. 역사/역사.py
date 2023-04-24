import sys

N, K = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(N + 1)]
INF = 10e6
d = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    d[a][b] = 1

for m in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            d[s][e] = min(d[s][e], d[s][m] + d[m][e])


M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if d[a][b] != INF:
        print(-1)
    elif d[b][a] != INF:
        print(1)
    else:
        print(0)