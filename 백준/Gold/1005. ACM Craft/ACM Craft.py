import sys
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, sys.stdin.readline().split())

    D = list(map(int, input().split()))
    in_degree = [0] * (N + 1)

    adjl = [[] for _ in range(N + 1)]
    adjl2 = [[] for _ in range(N + 1)]
    for _ in range(K):
        a, b = map(int, input().split())
        adjl[a].append(b)
        adjl2[b].append(a)
        in_degree[b] += 1
    W = int(input())

    T = [0]

    def topolo():
        visit = [0] * (N + 1)
        qu = deque()
        for i in range(1, N + 1):
            if in_degree[i] == 0:
                qu.append(i)
                visit[i] = 1
        while qu:
            nod = qu.popleft()
            T.append(nod)
            for nnod in adjl[nod]:
                if visit[nnod] == 0:
                    in_degree[nnod] -= 1
                    if in_degree[nnod] == 0:
                        visit[nnod] = 1
                        qu.append(nnod)
    topolo()
    dp = [0] * (N + 1)
    for i in T[1:]:
        if adjl2[i]:
            dp[i] = max(dp[j] for j in adjl2[i]) + D[i-1]
        else:
            dp[i] = D[i-1]

    print(dp[W])