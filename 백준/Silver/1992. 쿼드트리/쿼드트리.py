N = int(input())
array = [list(map(int, input())) for _ in range(N)]


def func(N, i, j):
    rep = array[i][j]
    if N == 1:
        return str(rep)
    for r in range(i, i + N):
        for c in range(j, j + N):
            # 다르면 분할하고 묶음으로 다시 받아줌.
            if array[r][c] != rep:
                return '(' + func(N // 2, i, j) + func(N // 2, i, j + N // 2) + func(N // 2, i + N // 2, j) + func(
                    N // 2, i + N // 2, j + N // 2) + ')'
    return str(rep)  # 전체 원소가 같으면 그냥 대표값으로 반환.


print(func(N, 0, 0))
