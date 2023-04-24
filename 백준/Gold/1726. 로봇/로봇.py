import sys
from collections import deque

def reachable(ci, cj, ni, nj):
    if ci == ni:
        if cj > nj:
            for j in range(cj - 1, nj - 1, - 1):
                if array[ci][j] == '1':
                    return False
        else:
            for j in range(cj + 1, nj + 1):
                if array[ci][j] == '1':
                    return False
        return True
    elif cj == nj:
        if ci > ni:
            for i in range(ci - 1, ni - 1, -1):

                if array[i][cj] == '1':
                    return False
        else:
            for i in range(ci + 1, ni + 1):

                if array[i][cj] == '1':
                    return False
        return True


N, M = map(int, sys.stdin.readline().split())
array = [sys.stdin.readline().split() for _ in range(N)]
si, sj, sd = map(int, sys.stdin.readline().split())
sd -= 1
si -= 1
sj -= 1
ei, ej, ed = map(int, sys.stdin.readline().split())
ed -= 1
ei -= 1
ej -= 1

INF = 10e6
visit = [[[INF] * 4 for _ in range(M)] for _ in range(N)]

qu = deque([(sd, si, sj)])
visit[si][sj][sd] = 1

while qu:
    cd, ci, cj = qu.popleft()
    di, dj = [(0, 1), (0, -1), (1, 0), (-1, 0)][cd]
    for length in range(1, 4):
        ni = di * length + ci
        nj = dj * length + cj
        if 0 <= ni < N and 0 <= nj < M and visit[ni][nj][cd] > visit[ci][cj][cd] + 1 and reachable(ci, cj, ni, nj):
            visit[ni][nj][cd] = visit[ci][cj][cd] + 1
            qu.append((cd, ni, nj))
    for nd in [[2, 3], [2, 3], [0, 1], [0, 1]][cd]:
        if visit[ci][cj][nd] > visit[ci][cj][cd] + 1:
            visit[ci][cj][nd] = visit[ci][cj][cd] + 1
            qu.append((nd, ci, cj))

print(visit[ei][ej][ed] - 1)