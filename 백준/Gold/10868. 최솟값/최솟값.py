import sys

N, M = map(int, sys.stdin.readline().split())
series = [int(sys.stdin.readline()) for _ in range(N)]
tree = {}


def func(start, end, nod):
    if start == end:
        tree[nod] = series[start]
        return tree[nod]
    mid = (start + end) // 2
    a = func(start, mid, nod * 2 + 1)
    b = func(mid + 1, end, nod * 2 + 2)
    tree[nod] = min(a, b)
    return tree[nod]


def query(start, end, left, right, nod):
    if left > end or start > right:
        return 10e9
    if left <= start and right >= end:
        return tree[nod]
    mid = (start + end) // 2
    return min(query(start, mid, left, right, nod * 2 + 1), query(mid + 1, end, left, right, nod * 2 + 2))


func(0, N - 1, 0)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(query(0, N - 1, a - 1, b - 1, 0))
