N = int(input())

lst = list(map(int, input().split()))
dp = [1] * N
dp[0] = 1
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if lst[i] > lst[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))
