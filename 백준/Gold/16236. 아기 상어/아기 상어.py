def get_distance():
    si, sj = shark.position
    qu = [(si, sj)]
    distances[si][sj] = 1
    while qu:
        ci, cj = qu.pop(0)
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and distances[ni][nj] == 0 and pool[ni][nj] <= shark.size:
                qu.append((ni, nj))
                distances[ni][nj] = distances[ci][cj] + 1


class Shark:
    def __init__(self):
        self.size = 2
        self.fish = 0
        self.position = (0, 0)

    def move(self, x, y):
        self.position = (x, y)

    def eat(self):
        self.fish += 1
        if self.fish == self.size and self.size != 7:
            self.size += 1
            self.fish = 0


N = int(input())
pool = [list(map(int, input().split())) for _ in range(N)]
shark = Shark()

for i in range(N):
    for j in range(N):
        if pool[i][j] == 9:
            shark.move(i, j)
            pool[i][j] = 0
distances = [[0] * N for _ in range(N)]

get_distance()
t = 0
d = 1
while d <= N * N:
    flag = False
    for r in range(shark.position[0] - d, shark.position[0] + d + 1):
        for c in range(shark.position[1] - d + abs(shark.position[0] - r),
                       shark.position[1] + d + 1 - abs(shark.position[0] - r)):
            if 0 <= r < N and 0 <= c < N and pool[r][c] != 0 and pool[r][c] < shark.size and distances[r][c] != 0 and distances[r][c] <= d + 1:
                shark.move(r, c)
                shark.eat()
                pool[r][c] = 0
                t += d
                d = 0
                distances = [[0] * N for _ in range(N)]
                get_distance()
                flag = True
                break
        if flag:
            break
    d += 1
print(t)