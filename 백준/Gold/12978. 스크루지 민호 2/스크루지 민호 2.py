import sys

sys.setrecursionlimit(2000000)

N = int(sys.stdin.readline())
adjl = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    adjl[a - 1].append(b - 1)
    adjl[b - 1].append(a - 1)
visit = [0] * N
dp = [[10e5, 10e5] for _ in range(N)]


def dfs(i):
    visit[i] = 1
    nxt_lst = [j for j in adjl[i] if visit[j] == 0]
    if not nxt_lst:
        # 경찰서가 없는 상태
        dp[i][0] = 0
        # 경찰서가 있는 상태
        dp[i][1] = 1
        return
    ans0 = 0
    ans1 = 0
    for j in nxt_lst:
        dfs(j)
        # 경찰서가 없는상태. 자식노들 전부 경찰서가 있어야 함.
        ans0 += dp[j][1]
        # 경찰서가 있는 상태. 아무거나 상관 없음
        ans1 += min(dp[j])
    dp[i][0] = ans0
    dp[i][1] = ans1 + 1
    return


dfs(0)
print(min(dp[0]))