import heapq

import sys


def dijkstra(limit):
    d = [INF] * (N + 1)
    q = [(1, 0)]  # 시작 위치, 회수
    while q:
        current_node, current_cost = heapq.heappop(q)
        if d[current_node] < current_cost:
            continue
        for next_node, value in adjl[current_node]:
            if value > limit:
                if current_cost + 1 < d[next_node]:
                    heapq.heappush(q, (next_node, current_cost + 1))
                    d[next_node] = current_cost + 1
            elif current_cost < d[next_node]:
                heapq.heappush(q, (next_node, current_cost))
                d[next_node] = current_cost
    if d[N] > K:
        return False
    return True

N, P, K = map(int, input().split())
adjl = [[] for _ in range(N + 1)]
INF = 1e9
key = 0
for _ in range(P):
    a, b, c = map(int, sys.stdin.readline().split())
    adjl[a].append((b, c))  # 는 b와 연결, 비용은 c
    adjl[b].append((a, c))


left, right = 0, 1000001
ans = -1
while left <= right:
    mid = (left + right) // 2
    flag = dijkstra(mid)
    if flag:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)