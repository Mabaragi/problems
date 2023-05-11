import sys
from bisect import bisect_right


N, M = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
cats = []
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    if i > N or j > M:
        continue
    cats.append((i, j))
cats.sort()
d = [cats[0][1]]
for i in range(1, len(cats)):
    r, c = cats[i]
    idx = bisect_right(d, c)
    if c >= d[-1]:
        d.append(c)
    else:
        d[idx] = c
print(len(d))
