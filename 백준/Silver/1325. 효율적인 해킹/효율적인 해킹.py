from collections import defaultdict, deque

import sys

N, M = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(N + 1)]

# A, B : A 가 B를 신뢰한다, B가 A를 해킹한다.
for _ in range(M):
    a, b = map(int, input().split())
    adjl[b].append(a)

cnt = [0] * (N + 1)
mx = 0
for i in range(1, N + 1):
    qu = deque([i])
    visit = [0] * (N + 1)
    visit[i] = 1
    while qu:
        current_node = qu.popleft()
        for next_node in adjl[current_node]:
            if not visit[next_node]:
                visit[next_node] = 1
                qu.append(next_node)
                cnt[i] += 1
    mx = max(mx, cnt[i])
result = [i for i in range(1, N + 1) if cnt[i] == mx]
print(*result)