from collections import deque


N, M = map(int, input().split())
adjl = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
parent = [i for i in range(N + 1)]
for _ in range(M):
    lst = list(map(int, input().split()))
    for i in range(2, lst[0] + 1):
        a, b = lst[i - 1], lst[i]
        adjl[a].append(b)
        in_degree[b] += 1

discovered = [-1] * (N + 1)
finished = [0] * (N + 1)
node_order = 0


def dfs(s):
    global node_order
    discovered[s] = node_order
    node_order += 1
    for e in adjl[s]:
        if discovered[e] == -1:
            dfs(e)
        elif finished[e] == 0:
            print(0)
            exit()
    finished[s] = 1


for i in range(1, N + 1):
    if discovered[i] == -1:
        dfs(i)

T = []
qu = deque([])
visit = [0] * (N + 1)
for i in range(1, N + 1):
    if in_degree[i] == 0:
        qu.append(i)
        visit[i] = 1

while qu:
    cn = qu.popleft()
    T.append(cn)
    for nn in adjl[cn]:
        if visit[nn] == 0:
            in_degree[nn] -= 1
            if in_degree[nn] == 0:
                visit[nn] = 1
                qu.append(nn)
for i in T:
    print(i)
