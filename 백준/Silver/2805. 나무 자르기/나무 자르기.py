N, K = map(int, input().split())
trees = list(map(int, input().split()))
left = 0
right = max(trees)
while left < right:
    mid = (left + right) // 2
    tree_amount = 0
    for tree in trees:
        tree_amount += max(0, tree - mid)
    if tree_amount < K:
        right = mid
    else:
        left = mid + 1
        ans = mid
print(ans)