N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

left = 1
right = houses[-1] - houses[0]

while left <= right:
    middle = (left + right) // 2
    sm = 1
    last_installed = houses[0]
    for i in range(1, N):
        if houses[i] >= last_installed + middle:
            sm += 1
            last_installed = houses[i]

    if sm >= C:
        left = middle + 1
        ans = middle
    else:
        right = middle - 1
print(ans)