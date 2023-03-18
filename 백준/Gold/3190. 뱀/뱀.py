import sys

from collections import deque

N = int(sys.stdin.readline())
array = [[0] * N for _ in range(N)]

K = int(sys.stdin.readline())
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    array[a - 1][b - 1] = 1

L = int(sys.stdin.readline())
cmd_lst = deque([])
for _ in range(L):
    a, b = sys.stdin.readline().split()
    cmd_lst.append((int(a), b))

snake = deque([(0, 0)])
dct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0

t = 0
while True:
    ci, cj = snake[-1]
    di, dj = dct[d]
    ni, nj = ci + di, cj + dj
    if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in snake:
        snake.append((ni, nj))
        if array[ni][nj] == 0:
            snake.popleft()
        else:
            array[ni][nj] = 0
    else:
        break
    t += 1
    if cmd_lst and t == cmd_lst[0][0]:
        cmd = cmd_lst.popleft()[1]
        if cmd == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

print(t + 1)
