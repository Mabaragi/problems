import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

qu = deque([N])


visit = [-1] * 100001
visit_pre = [-1] * 100001

visit[N] = 0

while qu:
    cn = qu.popleft()
    for nn in (cn - 1, cn + 1, 2 * cn):
        if 0 <= nn < 100001 and visit[nn] == -1:
            qu.append(nn)
            visit[nn] = visit[cn] + 1
            visit_pre[nn] = cn


ans = deque()
i = K
while i != -1:
    ans.appendleft(i)
    i = visit_pre[i]

print(visit[K])
print(*ans)