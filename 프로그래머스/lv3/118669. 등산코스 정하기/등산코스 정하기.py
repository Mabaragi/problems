from collections import deque
INF = int(10e9)


def solution(n, paths, gates, summits):
    summits.sort()
    gates_set = set(gates)
    summits_set = set(summits)
    N = n
    adjl = [[] for _ in range(N)]
    for path in paths:
        a, b, c = path
        adjl[a - 1].append((b - 1, c))
        adjl[b - 1].append((a - 1, c))
    
    
    # visit: 최소값으로 갱신 되어야함
    # cc: 최대값으로 갱신 되어야함
    
    visit = [INF] * N
    for s in gates:
        s -= 1
        visit[s] = 0
        qu = deque([(s, 0)])
        while qu:
            cn, cc = qu.popleft()
            if cc > visit[cn] or (cn != s and cn + 1 in gates_set) or cn + 1 in summits_set:
                continue
            for nn, nc in adjl[cn]:
                if nc < cc:
                    nc = cc
                if visit[nn] > nc:
                    visit[nn] = nc
                    qu.append((nn, nc))
    mn = INF
    for i in summits:
        if mn > visit[i - 1]:
            mn = visit[i - 1]
            mn_idx = i
    
    return [mn_idx, mn]