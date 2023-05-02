import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

coordinates = [(0, 0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)] + [(10000, 10000)]
distances = [[0] * (N + 2) for _ in range(N + 2)]

for i in range(N + 2):
    for j in range(N + 2):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        distances[i][j] = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** (1 / 2)


def bfs(volume):
    visit = [0] * (N + 2)
    qu = deque([(0, 0)])
    visit[0] = 1
    while qu:
        curr, cnt = qu.popleft()
        if distances[curr][N + 1] <= volume:
            return True
        if cnt == K:
            continue
        for j in range(1, N + 1):
            if i != j and distances[curr][j] <= volume and visit[j] == 0:
                visit[j] = 1
                qu.append((j, cnt + 1))


left = 0
right = 20000
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print((ans + 9) // 10)