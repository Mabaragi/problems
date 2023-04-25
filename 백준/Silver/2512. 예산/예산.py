N = int(input())
budgets = list(map(int, input().split()))
max_budget = int(input())
left = 0
right = max(budgets)

while left <= right:
    mid = (left + right)//2
    sm = 0
    for budget in budgets:
        sm += min (budget, mid)
    if sm <= max_budget:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)