import sys

def get_parent(parent, x):
    if parent[x] == x:
        return x
    return get_parent(parent, parent[x])


def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    return False


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(N + 1)]
edge_lst = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    adjl[a].append((c, b))
    adjl[b].append((c, a))
    edge_lst.append((c, a, b))
edge_lst.sort()
parent = [i for i in range(N + 1)]
ans = 0
for i in range(M):
    cost, start, end = edge_lst[i]
    if not find_parent(parent, start, end):
        union_parent(parent, start, end)
        ans += cost
print(ans)