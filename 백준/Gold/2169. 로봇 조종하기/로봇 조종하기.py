N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

# dp를 2가지 경우로 나뉘어서 생각. 각각 오른쪽, 왼쪽으로 가는 경우라고 생각
dp = [[[0] * 2 for _ in range(M)] for _ in range(N)]

for i in range(2):
    dp[0][0][i] = array[0][0]
    for j in range(1, M):
        dp[0][j][i] = dp[0][j - 1][i] + array[0][j]

# 각 행
for i in range(1, N):
    # 오른쪽으로 가는 경우
    dp[i][0][0] = max(dp[i - 1][0]) + array[i][0]
    for j in range(1, M):
        dp[i][j][0] = max(dp[i][j - 1][0], max(dp[i-1][j])) + array[i][j]

    # 왼쪽으로 가는 경우
    dp[i][-1][1] = max(dp[i-1][-1]) + array[i][-1]
    for j in range(M - 2, -1, -1):
        dp[i][j][1] = max(dp[i][j + 1][1], max(dp[i - 1][j])) + array[i][j]


print(max(dp[N - 1][M - 1]))
