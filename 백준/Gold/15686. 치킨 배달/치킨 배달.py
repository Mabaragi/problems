import sys

def func(i, r):
    global ans
    if i == M:  # M 번 다 지운 상태라면
        sm = 0
        for y in range(N):
            for x in range(N):
                if array[y][x] == 1:
                    sm += get_distance(y, x)
                    if sm > ans:
                        return
        if ans > sm:
            ans = sm
        return
    for k in range(r, N * N):
        if array[k // N][k % N] == 2:  # 치킨집이면 지우고 넘김
            array[k // N][k % N] = 0
            func(i + 1, k + 1)
            array[k // N][k % N] = 2


def get_distance(r, c):
    d = 0
    while True:
        d += 1
        for i in range(r - d, r + d + 1):
            for j in range(c - d + abs(r - i), c + d + 1 - abs(r - i)):
                if 0 <= i < N and 0 <= j < N:
                    if array[i][j] == 2:
                        return abs(r - i) + abs(c - j)


N, M = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 2:
            cnt += 1
M = cnt - M

ans = 2 * N ** 3
func(0, 0)
print(ans)
