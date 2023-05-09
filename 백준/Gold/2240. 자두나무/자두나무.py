import sys

N, M = map(int, sys.stdin.readline().split())
peaches = [int(sys.stdin.readline()) for _ in range(N)]


dp = [[0] * N for _ in range(M + 1)]

if peaches[0] == 1:
    dp[0][0] = 1
for i in range(1, N):
    if peaches[i] == 1:
        dp[0][i] += 1
    dp[0][i] += dp[0][i-1]

for i in range(1, M + 1):
    # i가 홀수일때 2여야함, i가 짝수일때 1이어야함
    dp[i][0] = 1 if i % 2 + 1 == peaches[0] else 0
    for j in range(1, N):
        plus = 1 if i % 2 + 1 == peaches[j] else 0
        dp[i][j] = max(dp[i - 1][j - 1] + plus, dp[i][j - 1] + plus)

print(max(dp[i][-1] for i in range(M + 1)))