from collections import deque

def get_min_distance(cluseter):
    for distance in range(1, N):
        for crystal in cluseter:
            i, j = crystal
            if i + distance >= N or ((i + distance, j) not in cluseter and array[i + distance][j] =='x'):
                return distance - 1


def get_cluster():
    k = -1
    visit = [[0] * M for _ in range(N)]
    clusters = {}
    for i in range(N - 1, - 1, - 1):
        for j in range(M):
            if array[i][j] == 'x' and visit[i][j] == 0:
                visit[i][j] = 1
                qu = deque([(i, j)])
                cluster = [(i, j)]
                k += 1
                while qu:
                    ci, cj = qu.popleft()
                    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < M and array[ni][nj] == 'x' and visit[ni][nj] == 0:
                            visit[ni][nj] = 1
                            qu.append((ni, nj))
                            cluster.append((ni, nj))
                clusters[k] = cluster
    return clusters


N, M = map(int, input().split())
array = [list(input()) for _ in range(N)]
K = int(input())
lst = list(map(int, input().split()))

for l in range(K):
    i = N - lst[l]
    if l % 2 == 0:
        for j in range(M):
            if array[i][j] == 'x':
                array[i][j] = '.'
                break
    else:
        for j in range(M - 1, - 1, - 1):
            if array[i][j] == 'x':
                array[i][j] = '.'
                break

    clusters = get_cluster()
    for i in clusters:
        if i == 0:
            continue
        cluster = clusters[i]
        cluster.sort(reverse=True)
        distance = get_min_distance(cluster)
        for i, j in cluster:
            array[i][j] = '.'
            array[i + distance][j] = 'x'

for i in array:
    print(''.join(i))
print()