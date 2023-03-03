r, c, k = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(3)]
r -= 1
c -= 1

def R(N, M):
    global array
    mxlen = 0
    lst2 = [[] for _ in range(N)]
    for r in range(N):
        lst = []
        cnt = [0] * 1000
        for c in range(M):
            if array[r][c] == 0:
                continue
            cnt[array[r][c]] += 1
            if array[r][c] not in lst:
                lst.append(array[r][c])
        lst.sort()
        lst.sort(key=lambda x: cnt[x])
        for i in lst:
            lst2[r].append(i)
            lst2[r].append(cnt[i])
        if mxlen < len(lst2[r]):
            mxlen = len(lst2[r])
    array = [[0] * mxlen for _ in range(N)]
    for i in range(N):
        for j in range(mxlen):
            if j >= len(lst2[i]):
                continue
            array[i][j] = lst2[i][j]


def C(N, M):
    global array
    mxlen = 0
    lst2 = [[] for _ in range(M)]
    for c in range(M):
        lst = []
        cnt = [0] * 1000
        for r in range(N):
            if array[r][c] == 0:
                continue
            cnt[array[r][c]] += 1
            if array[r][c] not in lst:
                lst.append(array[r][c])
        lst.sort()
        lst.sort(key=lambda x: cnt[x])
        for i in lst:
            lst2[c].append(i)
            lst2[c].append(cnt[i])
        if mxlen < len(lst2[c]):
            mxlen = len(lst2[c])
    array = [[0] * M for _ in range(mxlen)]
    for j in range(M):
        for i in range(mxlen):
            if i >= len(lst2[j]):
                continue
            array[i][j] = lst2[j][i]


N, M = 3, 3
t = 0
while r >= N or c >= M or array[r][c] != k:
    if N >= M:
        R(N, M)
    else:
        C(N, M)
    N = len(array)
    M = len(array[0])
    t += 1
    if t == 101:
        t = -1
        break
print(t)