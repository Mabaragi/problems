import sys


def to_num(ch):
    if ch.islower():
        return 1 + ord(ch) - ord('a')
    if ch.isupper():
        return 27 + ord(ch) - ord('A')
    if ch.isdigit():
        return int(ch)


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


N = int(input())
array = [list(map(to_num, input())) for _ in range(N)]
edges = []
for i in range(N):
    for j in range(N):
        if array[i][j] != 0 and i != j:
            edges.append((array[i][j], i, j))
edges.sort()
parent = [i for i in range(N)]
sm = sum([sum(i) for i in array])
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        sm -= c
for i in range(N):
    find(i)

if len(set(parent)) != 1:
    print(-1)
else:
    print(sm)
