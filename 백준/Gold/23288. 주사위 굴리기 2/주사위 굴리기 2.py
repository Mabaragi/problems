def get_point(i, j):
    global ans
    visit = [[0] * M for _ in range(N)]
    visit[i][j] = 1
    qu = [(i, j)]
    cnt = 1
    num = array[i][j]
    while qu:
        ci, cj = qu.pop(0)
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0 and array[ni][nj] == num:
                qu.append((ni, nj))
                visit[ni][nj] = 1
                cnt += 1
    ans += cnt * num


def move(dice, i, j):
    global dir
    if dir == 0:  # 오른쪽으로 향할 떄
        if j + 1 < M:
            pos[1] = j + 1
            dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
        else:
            pos[1] = j - 1
            dir = 2
            dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]
    elif dir == 1:  # 남쪽으로 향할 때
        if i + 1 < N:
            pos[0] = i + 1
            dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]
        else:
            pos[0] = i - 1
            dir = 3
            dice[5], dice[1], dice[0], dice[4] = dice[1], dice[0], dice[4], dice[5]
    elif dir == 2:  # 서쪽으로 향할 때
        if j - 1 >= 0:
            pos[1] = j - 1
            dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]
        else:
            pos[1] = j + 1
            dir = 0
            dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif dir == 3:  # 남쪽으로 향할 때
        if i - 1 >= 0:
            pos[0] = i - 1
            dice[5], dice[1], dice[0], dice[4] = dice[1], dice[0], dice[4], dice[5]
        else:
            pos[0] = i + 1
            dir = 1
            dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]


N, M, K = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]
dice = [1, 2, 3, 4, 5, 6]
dir = 0  # 0 동쪽방향 1 남쪽방향 2 서쪽방향 3 북쪽방향
pos = [0, 0]
ans = 0

for _ in range(K):
    move(dice, pos[0], pos[1])
    get_point(pos[0], pos[1])
    if dice[5] > array[pos[0]][pos[1]]:
        dir = (dir + 1) % 4
    elif dice[5] < array[pos[0]][pos[1]]:
        dir = (dir - 1) % 4

print(ans)
