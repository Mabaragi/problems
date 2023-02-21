N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0]


def func(N, i, j):
    global cnt
    rep = paper[i][j]
    for r in range(i, i + N):
        for c in range(j, j + N):
            if paper[r][c] != rep:
                func(N // 2, i, j)
                func(N // 2, i + N // 2, j)
                func(N // 2, i, j + N // 2)
                func(N // 2, i + N // 2, j + N // 2)
                return
    cnt[rep] += 1
    return


func(N, 0, 0)
print(cnt[0])
print(cnt[1])