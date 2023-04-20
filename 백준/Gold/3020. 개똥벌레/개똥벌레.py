import sys
N, H = map(int, sys.stdin.readline().split())


obstacles_top = [0] * (H + 1)
obstacles_bottom = [0] * (H + 1)

for _ in range(N // 2):
    obstacles_bottom[int(sys.stdin.readline())] += 1
    obstacles_top[H - int(sys.stdin.readline()) + 1] += 1

for i in range(H - 1, 0, - 1):
    obstacles_bottom[i] += obstacles_bottom[i + 1]


for i in range(2, H + 1):
    obstacles_top[i] += obstacles_top[i - 1]

obstacles = [obstacles_bottom[i] + obstacles_top[i] for i in range(1, H + 1)]
mn = min(obstacles)
cnt = obstacles.count(mn)
print(mn, cnt)