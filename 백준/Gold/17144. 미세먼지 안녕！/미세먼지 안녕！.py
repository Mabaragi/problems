R, C, T = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(R)]


def diffusion():
    narray = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if array[i][j] > 0:
                amount = array[i][j] // 5
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and array[ni][nj] != -1:
                        narray[ni][nj] += amount
                        array[i][j] -= amount
    for i in range(R):
        for j in range(C):
            narray[i][j] += array[i][j]
    return narray


def get_point(p):
    for i in range(R):
        if array[i][0] == p:
            return i


y = get_point(-1)


def circulation():
    array[y - 1][0] = array[y + 2][0] = 0
    for i in range(y - 2, -1, -1):
        array[i + 1][0], array[i][0] = array[i][0], 0
    for j in range(1, C):
        array[0][j - 1], array[0][j] = array[0][j], 0
    for i in range(1, y + 1):
        array[i - 1][C - 1], array[i][C - 1] = array[i][C - 1], 0
    for j in range(C - 2, 0, -1):
        array[y][j + 1], array[y][j] = array[y][j], 0

    for i in range(y + 3, R):
        array[i - 1][0], array[i][0] = array[i][0], 0
    for j in range(1, C):
        array[R - 1][j - 1], array[R - 1][j] = array[R - 1][j], 0
    for i in range(R - 2, y, -1):
        array[i + 1][C - 1], array[i][C - 1] = array[i][C - 1], 0
    for j in range(C - 2, 0, -1):
        array[y + 1][j + 1], array[y + 1][j] = array[y + 1][j], 0


for _ in range(T):
    array = diffusion()
    circulation()

print(sum([sum(i) for i in array]) + 2)