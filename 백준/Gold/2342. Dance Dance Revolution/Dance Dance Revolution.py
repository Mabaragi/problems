import sys

cmds = list(map(int, sys.stdin.readline().split()))
N = len(cmds)
costs = [[1, 2, 2, 2, 2],
         [2, 1, 3, 4, 3],
         [2, 3, 1, 3, 4],
         [2, 4, 3, 1, 3],
         [2, 3, 4, 3, 1], ]
INF = 4 * N
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(N + 1)]

dp[0][0][0] = 0
for i in range(1, N):
    cmd = cmds[i - 1]
    for l in range(5):
        for r in range(5):
            if dp[i - 1][l][r] != INF:
                if dp[i][cmd][r] > dp[i - 1][l][r] + costs[l][cmd]:
                    dp[i][cmd][r] = dp[i - 1][l][r] + costs[l][cmd]
                if dp[i][l][cmd] > dp[i - 1][l][r] + costs[r][cmd]:
                    dp[i][l][cmd] = dp[i - 1][l][r] + costs[r][cmd]

print(min(min(i for i in dp[N - 1])))