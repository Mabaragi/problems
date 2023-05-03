import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
INF = 1e10
d = [0] * (N + 1)

adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    adjl[a].append((b, c))
    adjl[b].append((a, c))
S, E = map(int, sys.stdin.readline().split())
d[S] = INF
heap = [(-INF, S)]

while heap:
    cl, cn = heapq.heappop(heap)
    cl *= -1
    if d[cn] > cl:
        continue
    for nn, nl in adjl[cn]:
        limit_load = min(cl, nl)
        if d[nn] < limit_load:
            d[nn] = limit_load
            heapq.heappush(heap, (-limit_load, nn))

print(d[E])
