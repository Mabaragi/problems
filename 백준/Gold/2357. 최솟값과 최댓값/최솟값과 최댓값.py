import sys
sys.setrecursionlimit(2000000)
N, M = map(int, sys.stdin.readline().split())
series = list(int(sys.stdin.readline()) for _ in range(N))
INF = 10e9
stree = [[0, 0] for _ in range(4 * N)]


def init(start, end, nod):
    # print(stree)
    mid = (start + end) // 2
    if start == end:
        stree[nod] = [series[start], series[start]]
        return
    init(start, mid, nod * 2)
    init(mid + 1, end, nod * 2 + 1)
    stree[nod] = [max(stree[nod * 2][0], stree[nod * 2 + 1][0]), min(stree[nod * 2][1], stree[nod * 2 + 1][1])]

    return


def query(left, right, start, end, nod):
    if right < start or left > end:
        return [0, INF]
    if left <= start and end <= right:
        return stree[nod]
    mid = (start + end) // 2
    left_val = query(left, right, start, mid, nod * 2)
    right_val = query(left, right, mid + 1, end, nod * 2 + 1)
    return [max(left_val[0], right_val[0]), min(left_val[1], right_val[1])]


init(0, N - 1, 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(*query(a - 1, b - 1, 0, N - 1, 1)[::-1])