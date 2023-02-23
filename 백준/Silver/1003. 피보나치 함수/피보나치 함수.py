T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    lst1 = [0] * (N + 3)
    lst1[1] = 1
    lst1[2] = 1

    for i in range(3, N + 1):
        lst1[i] = lst1[i - 1] + lst1[i - 2]

    print(lst1[N-1], lst1[N])
