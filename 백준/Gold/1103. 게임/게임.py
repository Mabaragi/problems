import sys

sys.setrecursionlimit(3000)
N, M = map(int, sys.stdin.readline().split())
board = [input() for _ in range(N)]
dp = {}


def func(i, j, d):
    if d > N * M:
        print(-1)
        exit()
    x = int(board[i][j])
    if (i, j) in dp:
        return dp[i, j]
    ans = 1
    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni, nj = i + x * di, j + x * dj
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 'H':
            ans = max(ans, func(ni, nj, d + 1) + 1)
    dp[i, j] = ans
    return ans


print(func(0, 0, 0))
