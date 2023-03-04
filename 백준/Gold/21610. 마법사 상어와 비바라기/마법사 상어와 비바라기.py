import sys

drc = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

N, M = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cmd_lst = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]


def get_water(i, j):
    for di, dj in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        ni, nj = di + i, dj + j
        if 0 <= ni < N and 0 <= nj < N and array[ni][nj] != 0:
            array[i][j] += 1


# 첫번째 구름
cloud_lst = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for cmd in cmd_lst:
    water = []
    d, s = cmd
    di, dj = drc[d]
    # 모든 구름이 이동한다.
    for cloud in cloud_lst:
        ci, cj = cloud
        ni, nj = (ci + s * di) % N , (cj + s * dj) % N
        array[ni][nj] += 1
        water.append((ni, nj))
    # 구름을 제거한다.
    cloud_lst = []
    # 물이 증가한 칸에 물 복사 마법을 시전한다.
    for i, j in water:
        get_water(i, j)
    # 물이 2 이상인 칸에 구름이 생긴다.
    for i in range(N):
        for j in range(N):
            if array[i][j] >= 2 and (i, j) not in water:
                cloud_lst.append((i, j))
                array[i][j] -= 2
ans = 0
for i in range(N):
    for j in range(N):
        ans += array[i][j]
print(ans)