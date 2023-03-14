import sys


def get_parent(p, a):
    if parent[a] == a:
        return a
    return (get_parent(p, p[a]))


def find_parent(p, a, b):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a == b:
        return True
    return False


def union(p, a, b):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(sys.stdin.readline())

stars = []
for _ in range(N):
    stars.append(tuple(map(float, sys.stdin.readline().split())))

parent = list(i for i in range(N + 1))
adjl = []

for i in range(N - 1):
    for j in range(i + 1, N):
        xi, yi = stars[i]
        xj, yj = stars[j]
        distance = (abs(xi - xj) ** 2 + abs(yi - yj) ** 2) ** (1 / 2)

        adjl.append((distance, i + 1, j + 1))
adjl.sort()

ans = 0
for i in adjl:
    distance, a, b = i
    if not find_parent(parent, a, b):
        union(parent, a, b)
        ans += distance
print(ans)