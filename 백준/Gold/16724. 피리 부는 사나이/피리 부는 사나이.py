import sys

sys.setrecursionlimit(10000)

def find(a):
    i, j = a
    if a == parent[i][j]:
        return a
    parent[i][j] = find(parent[i][j])
    return parent[i][j]


def union(a, b):
    a = find(a)
    b = find(b)
    ai, aj = a
    bi, bj = b
    if a < b:
        parent[ai][aj] = b
    else:
        parent[bi][bj] = a


N, M = map(int, input().split())
array = [list(input()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1), }
parent = [[(i, j) for j in range(M)] for i in range(N)]
ans = 0


for i in range(N):
    for j in range(M):
        D = array[i][j]
        di, dj = directions[D]
        union((i, j), (i + di, j + dj))


visit = set()
ans = 0
for i in range(N):
    for j in range(M):
        a, b = find((i, j))
        if (a, b) not in visit:
            visit.add((a, b))
            ans += 1
print(ans)
