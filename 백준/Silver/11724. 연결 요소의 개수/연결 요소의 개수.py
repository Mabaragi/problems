N, M = map(int, input().split())

adjl = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

visit = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):  # 각각의 미방문 노드에 대하여 BFS시행
    qu = []
    if visit[i] == 0:
        qu = [i]
        visit[i] = 1
    else:
        continue
    while qu:
        s = qu.pop(0)
        for j in adjl[s]:
            if visit[j] == 0:
                qu.append(j)
                visit[j] = visit[s] + 1
    cnt += 1
print(cnt)