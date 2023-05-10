import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
lst = [(0, 0)]
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((a, b))
lst.sort()
d = []
dp = [''] * (N + 1)
for i in range(1, N + 1):
    num, val = lst[i]
    idx = bisect_left(d, val)
    if idx >= len(d):
        d.append(val)
    else:
        d[idx] = val
    dp[idx + 1] = dp[idx] + str(num) + ','
set1 = set([i[0] for i in lst])
set2 = set(map(int, dp[len(d)].split(',')[:-1]))
ans = list(set1 - set2)
print(len(lst) - len(d) - 1)
for i in range(1, len(ans)):
    print(ans[i])