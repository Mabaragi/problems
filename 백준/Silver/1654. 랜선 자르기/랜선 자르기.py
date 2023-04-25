N, K = map(int, input().split())

lst = [int(input()) for _ in range(N)]
left = 1
right = max(lst)
ans = 1
while left < right:
    middle = (left + right)//2 + 1
    sm = 0
    for i in lst:
        sm += i//middle
    if sm >= K:
        left = middle
        ans = middle
    else:
        right = middle - 1

print(ans)