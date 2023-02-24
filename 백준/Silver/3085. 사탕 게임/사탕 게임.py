def func():
    mx = 0
    for i in range(N):
        cnt = 1
        for j in range(N - 1):
            if array[i][j] == array[i][j + 1]:
                cnt += 1
            else:
                if mx < cnt:
                    mx = cnt
                cnt = 1
        if mx < cnt:
            mx = cnt

    for j in range(N):
        cnt = 1
        for i in range(N - 1):
            if array[i][j] == array[i + 1][j]:
                cnt += 1
            else:
                if mx < cnt:
                    mx = cnt
                cnt = 1
        if mx < cnt:
            mx = cnt
    return mx


N = int(input())
array = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and array[i][j] != array[ni][nj]:
                array[i][j], array[ni][nj] = array[ni][nj], array[i][j]
                ans = max(ans, func())
                array[i][j], array[ni][nj] = array[ni][nj], array[i][j]
print(ans)
