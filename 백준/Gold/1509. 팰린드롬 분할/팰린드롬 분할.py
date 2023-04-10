st = input()
N = len(st)
dp = [[0] * (N) for _ in range(N)]
for length in range(1, N + 1):
    for start in range(N + 1 - length):
        if length == 1:
            dp[start][start] = 1
            continue
        end = start + length - 1
        if length == 2:
            if st[start] == st[end]:
                dp[start][end] = 1
        else:
            if st[start] == st[end] and dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

dp2 = [2500] * (N + 1)
dp2[0] = 0
for i in range(1, N + 1):
    temp = []
    for j in range(0, i + 1):
        if dp[j - 1][i - 1] == 1:
            temp.append(dp2[j - 1] + 1)
    dp2[i] = min(temp)
print(dp2[-1])