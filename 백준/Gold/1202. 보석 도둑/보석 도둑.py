import sys

import heapq

N, K = map(int, sys.stdin.readline().split())
items = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(items, (a, b))

bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

ans = 0
val = []
for bag in bags:
    while items and bag >= items[0][0]:
        heapq.heappush(val, -heapq.heappop(items)[1])
    if val:
        ans -= heapq.heappop(val)
    elif not items:
        break

print(ans)