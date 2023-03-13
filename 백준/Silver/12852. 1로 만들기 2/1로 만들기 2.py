import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)
dp[0] = (1, [0, 1])
dp[1] = (0, [1])

for i in range(2, N + 1):
    if i % 6 == 0:
        if dp[i // 3][0] <= dp[i // 2][0] and dp[i // 3][0] <= dp[i - 1][0]:
            dp[i] = (dp[i // 3][0] + 1, [i] + dp[i // 3][1])
        elif dp[i // 2][0] <= dp[i // 3][0] and dp[i // 2][0] <= dp[i - 1][0]:
            dp[i] = (dp[i // 2][0] + 1, [i] + dp[i // 2][1])
        else:
            dp[i] = (dp[i - 1][0] + 1, [i] + dp[i - 1][1])

    elif i % 3 == 0:
        if dp[i // 3][0] < dp[i - 1][0]:
            dp[i] = (dp[i // 3][0] + 1, [i] + dp[i // 3][1])
        else:
            dp[i] = (dp[i - 1][0] + 1, [i] + dp[i - 1][1])

    elif i % 2 == 0:
        if dp[i // 2][0] < dp[i - 1][0]:
            dp[i] = (dp[i // 2][0] + 1, [i] + dp[i // 2][1])
        else:
            dp[i] = (dp[i - 1][0] + 1, [i] + dp[i - 1][1])
    else:
        dp[i] = (dp[i - 1][0] + 1, [i] + dp[i - 1][1])
print(dp[N][0])
print(*dp[N][1])