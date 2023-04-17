import sys

N, M = map(int, sys.stdin.readline().split())
array = [[0] * (N + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        array[i][j] += array[i][j - 1]

for j in range(1, N + 1):
    for i in range(1, N + 1):
        array[i][j] += array[i - 1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(array[x2][y2] - array[x1 - 1][y2] - array[x2][y1 - 1] + array[x1 - 1][y1 - 1])