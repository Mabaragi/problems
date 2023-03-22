import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

qu = deque([N])


visit = [-1] * 100001
visit_cnt = [0] * 100001

visit[N] = 0
visit_cnt[N] = 1
while qu:
    cn = qu.popleft()
    for nn in (cn - 1, cn + 1, 2 * cn):
        if 0 <= nn < 100001 and (visit[nn] == -1 or visit[nn] == visit[cn] + 1):
            qu.append(nn)
            visit[nn] = visit[cn] + 1
            visit_cnt[nn] += 1

print(visit[K])
print(visit_cnt[K])