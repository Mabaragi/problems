N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
K = sum(lst2)
memories = [(lst2[i], lst[i]) for i in range(N)]
dp = [[0] * (N + 1) for _ in range(K + 1)]
for i in range(1, N + 1):
    c, m = memories[i - 1]
    for C in range(1, K + 1):
        if C < c:
            dp[C][i] = dp[C][i - 1]
        else:
            dp[C][i] = max(dp[C][i - 1], dp[C - c][i - 1] + m)
for c in range(1, K + 1):
    if dp[c][-1] >= M:
        ans = c
        break
print(ans)