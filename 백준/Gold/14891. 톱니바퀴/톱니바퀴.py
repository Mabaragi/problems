def rotate1(i, cmd):
    if rotated[i]:  # 이미 회전했으면 리턴
        return
    nt = (top[i] - 1 * cmd) % 8
    rotated[i] = True
    if i < 3 and gears[i][(top[i] + 2) % 8] != gears[i + 1][(top[i + 1] + 6) % 8]:
        rotate1(i + 1, -1 * cmd)
    if i > 0 and gears[i][(top[i] + 6) % 8] != gears[i - 1][(top[i - 1] + 2) % 8]:
        rotate1(i - 1, -1 * cmd)
    top[i] = nt


gears = [list(input()) for _ in range(4)]
top = [0 for _ in range(4)]
rotated = [False] * 4
K = int(input())

for _ in range(K):
    i, cmd = map(int, input().split())
    rotate1(i - 1, cmd)
    rotated = [False] * 4

ans = 0
for i in range(4):
    if gears[i][top[i]] == '1':
        ans += 2**i
print(ans)
