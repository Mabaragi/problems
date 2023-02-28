import sys

import heapq

"""
두 정점 v1, v2를 반드시 통과 해야 하는 최단경로.
이용했던 간선 다시 이용가능? 일반적인 데이크스트라랑 다름.
반드시 1 > v1 > v2 > N 또는 1 > v2 > v1 > N 경로를 취하게됨. 각 경로중에서 최단경로 3가지의 합중 짧은게 정답?
"""

N, E = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adjl[a].append((b, c))
    adjl[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().split())

def deik(snod, enod):
    if snod == enod:
        return 0
    d = [200000000] * (N + 1)
    d[snod] = 0
    heap = [(0, snod)]
    while heap:
        current_dis, current = heapq.heappop(heap)
        if d[current] < current_dis:
            pass
        for n, dis in adjl[current]:
            if d[n] > dis + d[current]:
                d[n] = dis + d[current]
                heapq.heappush(heap, (d[n], n))

    return d[enod]
ans = min(deik(1, v1) + deik(v1, v2) + deik(v2, N) ,deik(1, v2) + deik(v2, v1) + deik(v1, N))
if ans >= 200000000:
    print(-1)
else:
    print(ans)