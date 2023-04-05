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
T = deque([])


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
    T.appendleft(s)


for i in range(1, N + 1):
    if discovered[i] == -1:
        dfs(i)

for i in T:
    print(i)