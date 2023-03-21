N, M = map(int, input().split())

roads = []
parent = [i for i in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    roads.append((c, a, b))

roads.sort()


def union(a, b, parent):
    a = get_parent(a, parent)
    b = get_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



def get_parent(a, parent):
    if parent[a] == a:
        return a
    else:
        return get_parent(parent[a], parent)

ans = 0
for road in roads:
    cost, a, b, = road
    if get_parent(a, parent) == get_parent(b, parent):
        continue
    else:
        union(a, b, parent)
        ans += cost

print(ans)