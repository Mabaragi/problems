N, K = map(int, input().split())

lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))


ap = [[0] * (K + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    w, v = lst[i - 1]
    for j in range(1, K + 1):
        if j < w:
            ap[i][j] = ap[i-1][j]
        else:
            ap[i][j] = max(ap[i - 1][j], ap[i - 1][j-w] + v)
print(ap[N][K])