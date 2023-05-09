from copy import deepcopy

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

ans = 0


def merge_left_right(drc, array2):
    array = deepcopy(array2)
    merged = [[0] * N for _ in range(N)]
    if drc == 0:
        for i in range(N):
            for j in range(N - 2, -1, - 1):
                for k in range(j + 1, N):
                    if array[i][k] != 0:
                        if array[i][k] == array[i][j] and merged[i][k] == 0:
                            array[i][k], array[i][j] = 2 * array[i][k], 0
                            merged[i][k] = 1
                        else:
                            array[i][k - 1], array[i][j] = array[i][j], array[i][k - 1]
                        break
                else:
                    array[i][-1], array[i][j] = array[i][j], array[i][-1]

    elif drc == 1:
        for i in range(N):
            for j in range(N - 2, - 1, -1):
                for k in range(j + 1, N):
                    if array[k][i] != 0:
                        if array[k][i] == array[j][i] and merged[k][i] == 0:
                            array[k][i], array[j][i] = 2 * array[k][i], 0
                            merged[k][i] = 1
                        else:
                            array[k - 1][i], array[j][i] = array[j][i], array[k - 1][i]
                        break
                else:
                    array[-1][i], array[j][i] = array[j][i], array[-1][i]
    elif drc == 2:
        for i in range(N):
            for j in range(1, N):
                for k in range(j - 1, -1, -1):
                    if array[i][k] != 0:
                        if array[i][k] == array[i][j] and merged[i][k] == 0:
                            array[i][k], array[i][j] = 2 * array[i][k], 0
                            merged[i][k] = 1
                        else:
                            array[i][k + 1], array[i][j] = array[i][j], array[i][k + 1]
                        break
                else:
                    array[i][0], array[i][j] = array[i][j], array[i][0]
    elif drc == 3:
        for i in range(N):
            for j in range(1, N):
                for k in range(j - 1, -1, -1):
                    if array[k][i] != 0:
                        if array[k][i] == array[j][i] and merged[k][i] == 0:
                            array[k][i], array[j][i] = 2 * array[k][i], 0
                            merged[k][i] = 1
                        else:
                            array[k + 1][i], array[j][i] = array[j][i], array[k + 1][i]
                        break
                else:
                    array[0][i], array[j][i] = array[j][i], array[0][i]
    return array


def dfs(i, array):
    global ans
    if i >= 6:
        return
    val = max(max(j) for j in array)
    if ans < val:
        ans = val
    for j in range(4):
        nxt_array = merge_left_right(j, array)
        if nxt_array != array:
            dfs(i + 1, nxt_array)


dfs(0, array)

print(ans)
