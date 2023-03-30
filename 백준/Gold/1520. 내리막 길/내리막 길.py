N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
nums = []
for i in range(N):
    for j in range(M):
        nums.append((array[i][j], i, j))
nums.sort(reverse=True)
dp = [[0] * M for _ in range(N)]
dp[0][0] = 1

for num in nums:
    v, ci, cj = num
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M and array[ni][nj] < v:
            dp[ni][nj] += dp[ci][cj]

print(dp[-1][-1])