import sys

def floyd():
    for m in range(N):
        for s in range(N):
            if s == m:
                continue
            for e in range(N):
                if s == e or m == e:
                    continue
                if dist[s][e] > dist[s][m] + dist[m][e]:
                    dist[s][e] = dist[s][m] + dist[m][e]


def check():
    mn = 5000
    flag = False
    for i in range(N):
        for j in range(N):
            if i != j and adjm[i][j] != dist[i][j]:
                flag = True
                if mn > adjm[i][j]:
                    mn = adjm[i][j]
                    r, c = i, j
    if flag:
        return r, c
    return False


def get_min(lst):
    mn = 5000
    mn_lst = []
    for i in range(len(lst)):
        if lst[i] != 0 and mn > lst[i]:
            mn = lst[i]
            mn_lst = [i]
        elif mn == lst[i]:
            mn_lst.append(i)

    return mn, mn_lst


N = int(input())
adjm = []
INF = 1e9
dist = [[INF] * N for _ in range(N)]
ans = 0

for i in range(N):
    lst = list(map(int, input().split()))
    adjm.append(lst)
    mn, mn_lst = get_min(lst)
    for j in mn_lst:
        if dist[i][j] == INF and dist[j][i] == INF and i != j:
            dist[i][j] = mn
            dist[j][i] = mn
            ans += mn
floyd()

for _ in range(N ** 2 + 1):
    a = check()
    if a:
        r, c = a
        dist[r][c] = adjm[r][c]
        dist[c][r] = adjm[r][c]
        ans += adjm[r][c]
        floyd()
    else:
        print(ans)
        exit()
print(-1)
