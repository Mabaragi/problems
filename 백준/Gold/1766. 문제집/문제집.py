N, M = map(int, input().split())
in_degree = [0] * (N + 1)
adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    in_degree[b] += 1
T = []
visit = [0] * (N + 1)
while sum(in_degree) != 0:
    for i in range(1, N + 1):
        if visit[i] == 0 and in_degree[i] == 0:
            T.append(i)
            visit[i] = 1
            for j in adjl[i]:
                in_degree[j] -= 1
            break

for i in range(1, N + 1):
    if visit[i] == 0:
        T.append(i)
print(*T)
