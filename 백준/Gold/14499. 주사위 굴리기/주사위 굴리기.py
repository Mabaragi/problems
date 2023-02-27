def func(C):
    global di, dj
    if C == 4:  # 아래로 이동
        if 0 <= di + 1 < N:
            di += 1
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
            func2()
    elif C == 3:  # 위로 이동
        if 0 <= di - 1 < N:
            di -= 1
            dice[1], dice[5], dice[0], dice[4] = dice[0], dice[1], dice[4], dice[5]
            func2()
    elif C == 1:  # 오른쪽 이동
        if 0 <= dj + 1 < M:
            dj += 1
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
            func2()
    elif C == 2:  # 왼쪽 이동
        if 0 <= dj - 1 < M:
            dj -= 1
            dice[3], dice[0], dice[5], dice[2] = dice[0], dice[2], dice[3], dice[5]
            func2()


def func2():
    if array[di][dj] == 0:
        array[di][dj] = dice[5]
    else:
        dice[5] = array[di][dj]
        array[di][dj] = 0
    print(dice[0])


N, M, r, c, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))
dice = [0] * 6
di, dj = r, c
for i in cmd:
    func(i)