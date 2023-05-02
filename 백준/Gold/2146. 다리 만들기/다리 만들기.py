from collections import deque

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

# 섬들찾기
visit = [[0] * N for _ in range(N)]
islands = []
counter = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 1 and visit[i][j] == 0:
            counter += 1
            visit[i][j] = counter
            qu = deque([(i, j)])
            islands.append((i, j, counter))
            while qu:
                ci, cj = qu.popleft()
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < N and array[ni][nj] == 1 and visit[ni][nj] == 0:
                        visit[ni][nj] = counter
                        qu.append((ni, nj))
                        islands.append((ni, nj, counter))

# 섬들간의 최소거리 찾기
min_distance = 2000
for i in range(len(islands) - 1):
    for j in range(i + 1, len(islands)):
        li, lj, lc = islands[i]
        ri, rj, rc = islands[j]
        if lc == rc:
            continue
        if min_distance > abs(li - ri) + abs(lj - rj):
            min_distance = abs(li - ri) + abs(lj - rj)

print(min_distance - 1)