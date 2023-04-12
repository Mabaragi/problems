N = int(input())
lst = list(map(int, input().split()))
adjl = [[] for _ in range(N)]
for i in range(1, N):
    adjl[lst[i]].append(i)
dp = [-1] * N


def dfs(i):
    if not adjl[i]:
        dp[i] = 0
        return
    ans = len(adjl[i])
    for j in adjl[i]:
        dfs(j)

    temp_lst = sorted(adjl[i], key=lambda x: dp[x], reverse=True)
    for j in range(len(temp_lst)):
        dp[i] = max(dp[i], dp[temp_lst[j]] + j + 1)


dfs(0)
print(dp[0])