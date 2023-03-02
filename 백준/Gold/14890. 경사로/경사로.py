N, L = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
cnt = 0

def check(r):
    for c in range(N - 1):
        if array[r][c + 1] >= array[r][c] + 2:
            return False
        if array[r][c + 1] == array[r][c] + 1:
            if c - L < - 1:
                return False
            for k in range(L):
                if array[r][c - k] != array[r][c] or visit[r][c - k] == 1:
                    return False

            else:
                for k in range(L):
                    visit[r][c - k] = 1
    for c in range(N - 1, 0, -1):
        if array[r][c - 1] >= array[r][c] + 2:
            return False
        if array[r][c - 1] == array[r][c] + 1:
            if c + L > N:
                return False
            for k in range(L):
                if array[r][c + k] != array[r][c] or visit[r][c + k] == 1:
                    return False
            else:
                for k in range(L):
                    visit[r][c + k] = 1
    return True
for r in range(N):
    if check(r):
        cnt += 1


for i in range(N):
    for j in range(N):
        if i > j:
            array[i][j], array[j][i] = array[j][i], array[i][j]
            visit[i][j], visit[j][i] = visit[j][i], visit[i][j]

for i in range(N):
    for j in range(N):
        visit[i][j] = 0

for r in range(N):
    if check(r):
        cnt += 1
print(cnt)