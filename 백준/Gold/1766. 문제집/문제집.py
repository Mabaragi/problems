import heapq

N, M = map(int, input().split())
in_degree = [0] * (N + 1)
adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    in_degree[b] += 1
T = []
qu = []
for i in range(1, N + 1):
    if in_degree[i] == 0:
        qu.append(i)
while qu:
    current_nod = heapq.heappop(qu)
    T.append(current_nod)
    for next_nod in adjl[current_nod]:
        in_degree[next_nod] -= 1
        if in_degree[next_nod] == 0:
            heapq.heappush(qu, next_nod)
print(*T)