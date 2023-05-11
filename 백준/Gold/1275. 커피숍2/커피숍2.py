import sys
sys.setrecursionlimit(100000)

def init(start, end, nod):
    if start == end:
        segment_tree[nod] = lst[start]
        return segment_tree[nod]
    mid = (start + end) // 2
    left = init(start, mid, nod * 2)
    right = init(mid + 1, end, nod * 2 + 1)
    segment_tree[nod] = left + right
    return left + right


def query(start, end, left, right, nod):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return segment_tree[nod]
    mid = (start + end) // 2
    return query(start, mid, left, right, nod * 2) + query(mid + 1, end, left, right, nod * 2 + 1)


def update(start, end, nod, target, val):
    if target < start or end < target:
        return
    segment_tree[nod] += val - lst[target]
    if start == end and start == target:
        segment_tree[nod] = val
        return val
    mid = (start + end) // 2
    update(start, mid, nod * 2, target, val)
    update(mid + 1, end, nod * 2 + 1, target, val)


N, M = map(int, sys.stdin.readline().split())
lst = [0] + list(map(int, sys.stdin.readline().split()))
segment_tree = [0] * (4 * N)
init(1, N, 1)
for _ in range(M):
    x, y, a, b = map(int, sys.stdin.readline().split())
    if y < x:
        x, y, = y, x
    print(query(1, N, x, y, 1))
    update(1, N, 1, a, b)
    lst[a] = b