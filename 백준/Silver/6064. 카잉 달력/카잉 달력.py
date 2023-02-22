T = int(input())
for tc in range(1, T + 1):
    N, M, x, y = map(int, input().split())
    ans = - 1
    for i in range(0, N * M + 1, N):
        if (i + x) % M == y % M:
            ans = i + x
            break

    print(ans)