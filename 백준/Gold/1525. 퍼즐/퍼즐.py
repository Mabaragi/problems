from collections import deque

array = [list(input().split()) for _ in range(3)]


def to_list(st):
    lst1 = []
    for i in range(3):
        lst2 = []
        for j in range(3):
            lst2.append(st[i * 3 + j])
        lst1.append(lst2)
    return lst1


def get_zero(array):
    for i in range(3):
        for j in range(3):
            if array[i][j] == '0':
                return (i, j)


def to_string(lst):
    st = ''
    for i in lst:
        st += ''.join(i)
    return st


ci, cj = get_zero(array)

qu = deque([to_string(array)])
visit = {}
visit[to_string(array)] = 0

while qu:
    curr = qu.popleft()
    clst = to_list(curr)
    if curr == '123456780':
        print(visit[curr])
        exit()
    ci, cj = get_zero(clst)
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            clst[ci][cj], clst[ni][nj] = clst[ni][nj], clst[ci][cj]
            nstr = to_string(clst)
            if nstr not in visit or visit[nstr] > visit[curr] + 1:
                visit[nstr] = visit[curr] + 1
                qu.append(nstr)
            clst[ci][cj], clst[ni][nj] = clst[ni][nj], clst[ci][cj]
print(-1)