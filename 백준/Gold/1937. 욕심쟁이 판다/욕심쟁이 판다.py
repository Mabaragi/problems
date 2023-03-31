import sys, heapq
N = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
heap = []
for i in range(N):
    for j in range(N):
        heapq.heappush(heap, (array[i][j], i, j))
visit = [[1] * N for _ in range(N)]
mx = 1
while heap:
    v, i, j = heapq.heappop(heap)
    t = []
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and array[ni][nj] < array[i][j]:
            t.append((visit[ni][nj]))
    if t:
        visit[i][j] = max(t) + 1
print(max([max(i) for i in visit]))
