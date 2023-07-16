import sys

N = int(input())
lst = list(map(int, input().split()))
prefix_sum_right = [lst[0]] * N
for i in range(N - 1):
    prefix_sum_right[i + 1] = prefix_sum_right[i] + lst[i + 1]

ans1 = prefix_sum_right[-1] - prefix_sum_right[0] + max(prefix_sum_right[-1] -prefix_sum_right[i] - lst[i] for i in range(1, N - 1))
ans2 = prefix_sum_right[-2] + max(prefix_sum_right[i] - 2 * lst[i] for i in range(1, N - 1))
ans3 = max(prefix_sum_right[i] - prefix_sum_right[0] + prefix_sum_right[-2] - prefix_sum_right[i - 1] for i in range(1, N - 1))
print(max(ans1, ans2, ans3))