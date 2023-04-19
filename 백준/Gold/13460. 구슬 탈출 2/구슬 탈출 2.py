from collections import deque

def tilt(drc, array):
    array = [list(i) for i in array]
    di, dj = [(0, 1), (1, 0), (0, -1), (-1, 0)][drc]
    # 빨간공 움직이기
    ri, rj = get_point('R', array)
    ci, cj = ri, rj
    success = False
    fail = False
    while True:
        ni, nj = ci + di, cj + dj
        if array[ni][nj] == 'O':
            success = True
        if array[ni][nj] == '#' or array[ni][nj] == 'B':
            break
        ci, cj = ni, nj
    array[ri][rj] = '.'
    if not success:
        array[ci][cj] = 'R'
    # 파란 공 움직이기
    bi, bj = get_point('B', array)
    ci, cj = bi, bj
    while True:
        ni, nj = ci + di, cj + dj
        if array[ni][nj] == 'O':
            fail = True
        if array[ni][nj] == '#' or array[ni][nj] == 'R':
            break
        ci, cj = ni, nj
    array[bi][bj] = '.'
    array[ci][cj] = 'B'

    if not success:
        ri, rj = get_point('R', array)
        ci, cj = ri, rj
        while True:
            ni, nj = ci + di, cj + dj
            if array[ni][nj] == 'O':
                success = True
            if array[ni][nj] == '#' or array[ni][nj] == 'B':
                break
            ci, cj = ni, nj
        array[ri][rj] = '.'
        if not success:
            array[ci][cj] = 'R'
    if fail:
        return None
    if success:
        return 'Success'

    return [''.join(i) for i in array]


def get_point(p, array):
    for i in range(N):
        for j in range(M):
            if array[i][j] == p:
                return i, j


def to_string(array):
    result = ''
    for i in array:
        result += i
    return result


N, M = map(int, input().split())
array = [input() for _ in range(N)]

visit = {}
visit[to_string(array)] = 0
qu = deque([array])
ans = - 1
while qu:
    current_array = qu.popleft()
    if visit[to_string(current_array)] > 9:
        break
    for drc in range(4):
        next_array = tilt(drc, current_array)
        if next_array == 'Success':
            print(visit[to_string(current_array)] + 1)
            exit()
        if next_array and to_string(next_array) not in visit:
            qu.append(next_array)
            visit[to_string(next_array)] = visit[to_string(current_array)] + 1

print(ans)

