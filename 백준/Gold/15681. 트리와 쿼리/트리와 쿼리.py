import sys

sys.setrecursionlimit(100000)
def func(i):
    ans = 0
    if i in dp:
        return dp[i]
    for j in adjl[i]:
        if visit[j] == 0:
            visit[j] = 1
            ans += func(j)
    if ans:
        dp[i] = ans + 1
        return ans + 1
    dp[i] = 1
    return 1


# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.
N, R, Q = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    adjl[a - 1].append(b - 1)
    adjl[b - 1].append(a - 1)
visit = [0] * N
visit[R - 1] = 1
dp = {}
func(R - 1)
for _ in range(Q):
    k = int(sys.stdin.readline())
    print(dp[k - 1])