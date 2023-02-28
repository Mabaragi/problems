import sys

import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    adjl[a].append([b, c])
S, E = map(int, sys.stdin.readline().split())
d = [1000000000] * (N + 1)
d[S] = 0
S
heap = [(0, S)]
while heap:
    ccost, c = heapq.heappop(heap)
    if d[c] < ccost:
        continue
    for nod, cost in adjl[c]:
        if d[nod] > cost + d[c]:
            d[nod] = cost + d[c]
            heapq.heappush(heap, (d[nod], nod))

print(d[E])
