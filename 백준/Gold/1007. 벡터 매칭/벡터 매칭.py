from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    lst = list(combinations(points, N // 2))

    mn = 20000000
    for i in range(len(lst) // 2):
        sum_x = sum_y = 0
        for plus in lst[i]:
            sum_x += plus[0]
            sum_y += plus[1]
        for minus in lst[len(lst) - 1 - i]:
            sum_x -= minus[0]
            sum_y -= minus[1]
        result = (sum_x ** 2 + sum_y ** 2) ** (1 / 2)
        if mn > result:
            mn = result
    print(mn)
