import sys

N, K = map(int, sys.stdin.readline().split())

lst = []

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    lst.append((W, V))


dp = [[0] * (N + 1) for _ in range(K + 1)]

for j in range(1, N + 1):
    for i in range(1, K + 1):
        w, v = lst[j - 1]
        # print(w, v)
        if i < w:
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - w][j-1] + v)

print(dp[K][N])