from collections import deque

N, M = map(int, input().split())
adjl = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    in_degree[b] += 1
visit = [0] * (N + 1)
qu = deque([])
for i in range(1, N + 1):
    if in_degree[i] == 0:
        qu.append(i)
        visit[i] = 1
T = []
while qu:
    cn = qu.popleft()
    T.append(cn)
    for nn in adjl[cn]:
        if visit[nn] == 0:
            in_degree[nn] -= 1
            if in_degree[nn] == 0:
                qu.append(nn)
print(*T)