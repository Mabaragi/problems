from collections import deque

N, M = map(int, input().split())
adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
visit = [0] * (N + 1)
finished = [0] * (N + 1)
T = deque([])


def dfs(s):
    visit[s] = 1
    for e in adjl[s]:
        if visit[e] == 0:
            dfs(e)
    T.appendleft(s)


for i in range(1, N + 1):
    if visit[i] == 0:
        dfs(i)
print(*T)