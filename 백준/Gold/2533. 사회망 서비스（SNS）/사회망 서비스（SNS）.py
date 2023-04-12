import sys

N = int(sys.stdin.readline())
# 양방향 트리
adjl = [[] for _ in range(N)]
# 단방향트리. dfs 돌면서 만들거임
adjl2 = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    adjl[a - 1].append(b - 1)
    adjl[b - 1].append(a - 1)
visit = [0] * N
dp = {}
visit[0] = 1
stk = [0]
while len(stk) >= 1:
    current = stk[-1]
    for nxt in adjl[current]:
        if visit[nxt] == 0:
            visit[nxt] = 1
            stk.append(nxt)
            # 단방향 트리 만들기
            adjl2[current].append(nxt)
            current = nxt
            break
    else:
        if not adjl2[current]:
            dp[current, 1] = 1
            dp[current, 0] = 0
        else:
            ans1 = 1
            ans0 = 0
            for nxt in adjl2[current]:
                ans1 += min(dp[nxt, 0], dp[nxt, 1])
                ans0 += dp[nxt, 1]
            dp[current, 1] = ans1
            dp[current, 0] = ans0
        stk.pop()
print(min(dp[0, 0], dp[0, 1]))