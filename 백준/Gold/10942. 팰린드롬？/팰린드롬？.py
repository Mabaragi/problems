import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [[0] * (N) for _ in range(N)]
for length in range(1, N + 1):
    for start in range(N + 1 - length):
        if length == 1:
            dp[start][start] = 1
            continue
        end = start + length - 1
        if lst[start] == lst[end]:
            if length == 2:
                dp[start][end] = 1
            else:
                if dp[start + 1][end - 1] == 1:
                    dp[start][end] = 1
M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a - 1][b - 1])