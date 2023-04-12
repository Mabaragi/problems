import sys

sys.setrecursionlimit(2000000)

N = int(sys.stdin.readline())
villagers = list(map(int, sys.stdin.readline().split()))
adjl = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    adjl[a - 1].append(b - 1)
    adjl[b - 1].append(a - 1)

dp = [[-10e9] * 3 for _ in range(N)]
visit = [0] * N


def dfs(i):
    visit[i] = 1
    nxt_lst = [j for j in adjl[i] if visit[j] == 0]
    if not nxt_lst:
        # i가 우수 마을인 경우
        dp[i][0] = villagers[i]
        # i가 우수 마을이며 인접 우수 마을이 없는 경우
        dp[i][1] = 0
        return

    ans0 = 0
    ans1 = 0
    ans2 = 0
    for j in nxt_lst:
        dfs(j)
        ans0 += max(dp[j][1:])
        ans1 += dp[j][2]
        ans2 += max(dp[j][0], dp[j][2])
    ans2 = max([ans2 - max(dp[j][0], dp[j][2]) + dp[j][0] for j in nxt_lst])
    dp[i][0] = ans0 + villagers[i]
    dp[i][1] = ans1
    dp[i][2] = ans2


dfs(0)
print(max(dp[0][0], dp[0][2]))
