N, M = map(int, input().split())

r, c, id = map(int, input().split())
dl = [(-1, 0), (0, 1), (1, 0), (0, -1)]
room = [list(map(int, input().split())) for _ in range(N)]


class Robot:
    def __init__(self):
        self.dir = id
        self.position = (r, c)
        self.cnt = 0

    def work(self):
        while True:
            flag = False
            ci, cj = self.position
            if room[ci][cj] == 0:
                room[ci][cj] = 2
                self.cnt += 1


            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ti, tj = ci + di, cj + dj
                if room[ti][tj] == 0:
                    for k in range(4):
                        self.dir = (self.dir - 1) % 4
                        zi, zj = dl[self.dir]
                        ni, nj = ci + zi, cj + zj
                        if room[ni][nj] == 0:
                            self.position = (ni, nj)
                            flag = True
                            break
                if flag:
                    break

            else:
                zi, zj = dl[self.dir]
                ni, nj = ci - zi, cj - zj
                if room[ni][nj] == 1:
                    return
                else:
                    self.position = ni, nj

robot = Robot()
robot.work()
print(robot.cnt)