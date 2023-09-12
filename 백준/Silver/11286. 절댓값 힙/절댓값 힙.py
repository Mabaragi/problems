import sys

import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    I = int(sys.stdin.readline())
    if I == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print('0')
    else:
        heapq.heappush(heap, (abs(I), I))