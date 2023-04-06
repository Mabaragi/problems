R, C, M = map(int, input().split())
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([z, s, d, r - 1, c - 1])

sharks.sort(reverse=True)
drc = [0, (-1, 0), (1, 0), (0, 1), (0, -1)]

turn = [0, 2, 1, 4, 3]


def move(r, c, speed, d):
    di, dj = drc[d]
    r_distance = di * speed
    c_distance = dj * speed
    while r_distance != 0:
        if r_distance > 0:
            # 범위 안이면 그냥 이동
            if r_distance + r < R:
                nr = r + r_distance
            # 범위 밖이면 경계로 이동
            else:
                d = turn[d]
                nr = R - 1
            # 거리 소모
        else:
            if r_distance + r >= 0:
                nr = r + r_distance
            else:
                d = turn[d]
                nr = 0
        r_distance -= nr - r
        r_distance *= -1
        r = nr
    while c_distance != 0:
        if c_distance > 0:
            # 범위 안이면 그냥 이동
            if c_distance + c < C:
                nc = c + c_distance
            # 범위 밖이면 경계로 이동
            else:
                d = turn[d]
                nc = C - 1
            # 거리 소모
        else:
            if c_distance + c >= 0:
                nc = c + c_distance
            else:
                d = turn[d]
                nc = 0
        c_distance -= nc - c
        c_distance *= -1
        c = nc
    return r, c, d

ans = 0
for T in range(C):
    # 상어 잡기
    mn = R
    catch = 0
    for shark in sharks:
        *head, i, j = shark
        if j == T and mn > i:
            mn = i
            catch = shark
    if catch:
        # print('잡았다!', catch)
        ans += catch[0]
        sharks.remove(catch)

    # 상어 이동, 먹기
    next_sharks = []
    check = {}
    for shark in sharks:
        size, speed, d, i, j = shark
        ni, nj, nd = move(i, j, speed, d)
        if (ni, nj) not in check:
            next_sharks.append([size, speed, nd, ni, nj])
            check[ni, nj] = 1
    # print(check)
    sharks = next_sharks[:]
    next_sharks = []
    # sharks.sort(reverse=True)
    # print(sharks)
print(ans)