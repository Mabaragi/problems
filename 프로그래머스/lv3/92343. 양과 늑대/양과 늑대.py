from copy import deepcopy

ans = 0

def solution(info, edges):
    N = len(info)
    adjl = [[] for _ in range(N)]
    for edge in edges:
        a, b = edge
        adjl[a].append(b)
        adjl[b].append(a)

    dp = {}

    def dfs(sheep, wolf, nod, s_info):
        global ans
        n_info = deepcopy(s_info)
        if n_info[nod] == 0:
            sheep += 1
            n_info[nod] = -1
        elif n_info[nod] == 1:
            wolf += 1
            n_info[nod] = -1

        if (sheep, wolf, nod, tuple(n_info)) in dp:
            return
        dp[sheep, wolf, nod, tuple(n_info)] = 1

        if wolf >= sheep:
            return

        if nod == 0 and sheep > ans:
            ans = sheep


        for j in adjl[nod]:
            dfs(sheep, wolf, j, n_info)

    dfs(0, 0, 0, info)
    return ans