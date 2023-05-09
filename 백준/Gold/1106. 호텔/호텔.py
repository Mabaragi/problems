import sys


C, N = map(int, sys.stdin.readline().split())

lst = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * 200000

for i in range(1, 200000):
    for j in range(N):
        cost, val = lst[j]
        if i >= cost:
            dp[i] = max(dp[i], dp[i - cost] + val)
        else:
            dp[i] = max(dp[i], dp[i - 1])
    if dp[i] >= C:
        print(i)
        exit()
