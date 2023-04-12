T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    if N == 1:
        print(0)
        exit()

    adjl = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        adjl[a - 1].append((b - 1, c))
        adjl[b - 1].append((a - 1, c))

    visit = [0] * N
    def dfs(curr):
        visit[curr] = 1
        nxt_lst = [nxt for nxt in adjl[curr] if visit[nxt[0]] == 0]
        if not nxt_lst:
            return 10e9
        ans = 0
        for nxt, cost in nxt_lst:
            ans += min(cost, dfs(nxt))
        return ans

    print(dfs(0))
