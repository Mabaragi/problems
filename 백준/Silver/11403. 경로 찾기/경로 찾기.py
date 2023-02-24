N = int(input())
adjm = [list(map(int, input().split())) for _ in range(N)]

ansm = [[0] * N for _ in range(N)]
for i in range(N):  # 각각의 정점으로 시작
    visit = [0] * N
    qu = [i]
    while qu:
        c = qu.pop(0)
        for j in range(N):
            if adjm[c][j] == 1 and visit[j] == 0:
                visit[j] = 1
                qu.append(j)
                ansm[i][j] = 1
for i in ansm:
    print(*i)
