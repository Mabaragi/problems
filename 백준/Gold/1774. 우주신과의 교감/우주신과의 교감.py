import sys

def find(a):  # 최고 부모를 찾는 함수
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a



#  모든 점 간의 거리를 계산해놓으면 N^2 = 1000000 충분히 가능
N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N)]
points = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    union(a - 1, b - 1)
edges = []
for i in range(N - 1):
    for j in range(i + 1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        edges.append([i, j, ((x1-x2)**2 + (y1-y2)**2)**(1/2)])
edges.sort(key=lambda x:x[2])
ans = 0
for edge in edges:
    a, b, distance = edge
    if find(a) != find(b):
        union(a, b)
        ans += distance
print(f"{ans:.2f}")