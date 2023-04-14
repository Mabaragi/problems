import sys
sys.setrecursionlimit(10000)

N, M, K = map(int, sys.stdin.readline().split())
series = [0] + [int(sys.stdin.readline()) for _ in range(N)]
stree = [0] * (4 * N)
div = 1000000007

def init(start, end, nod):
    if start == end:
        stree[nod] = series[start]
        return stree[nod]
    mid = (start + end) // 2
    stree[nod] = (init(start, mid, nod * 2) * init(mid + 1, end, nod * 2 + 1)) % div
    return stree[nod]


def fix(target, value, start, end, nod):
    if end < target or target < start:
        return stree[nod]
    if start == target and target == end:
        stree[nod] = value
        return stree[nod]
    mid = (start + end) // 2
    stree[nod] = (fix(target, value, start, mid, nod * 2) * fix(target, value, mid + 1, end, nod * 2 + 1)) % div
    return stree[nod]


def query(left, right, start, end, nod):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return stree[nod]
    mid = (start + end) // 2
    return (query(left, right, start, mid, nod * 2) * query(left, right, mid + 1, end, nod * 2 + 1)) % div


init(1, N, 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        if series[b] == 0:
            series[b] = c
            init(1, N, 1)
        else:
            fix(b, c, 1, N, 1)
            series[b] = c
    else:
        print(query(b, c, 1, N, 1) % div)