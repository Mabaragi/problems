import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    adjl[a].append((b, c))
    adjl[b].append((a, c))

S, E = map(int, sys.stdin.readline().split())


def bfs(load):
    qu = deque([S])
    visit = [0] * (N + 1)
    visit[S] = 1
    while qu:
        curr = qu.popleft()
        for nxt, nxt_limit_load in adjl[curr]:
            if load <= nxt_limit_load and visit[nxt] == 0:
                visit[nxt] = 1
                if nxt == E:
                    return True
                qu.append(nxt)
    return False


left = 1
right = int(1e9)
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)
