import sys

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N)]
ans = 0
for i in range(1, M + 1):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        ans = i
        break
    else:
        union(a, b)

print(ans)