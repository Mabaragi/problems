def func(N, i, j):
    if N <= 3:
        base[i][j + 2] = '*'
        base[i + 1][j + 1] = base[i + 1][j + 3] = '*'
        # base[i+2][j:5] = '*****'
        for c in range(5):
            base[i + 2][j + c] = '*'
        return

    func(N // 2, i + N // 2, j)
    func(N // 2, i, j + N // 2)
    func(N // 2, i + N // 2, j + 2 * (N // 2))


N = int(input())
base = [[' '] * 2 * N for _ in range(N)]
func(N, 0, 0)
for i in base:
    print(''.join(i))
