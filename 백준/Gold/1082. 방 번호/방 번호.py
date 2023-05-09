INF = 1e6
N = int(input())
rooms = list(map(int, input().split()))
M = int(input())
dp = [-INF] * (M + 1)

for i in range(N - 1, - 1, -1):
    for j in range(rooms[i], M + 1):
        dp[j] = max(dp[j - rooms[i]] * 10 + i, i, dp[j])

print(dp[M])