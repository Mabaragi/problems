from bisect import bisect_left

N, M = map(int, input().split())
K = int(input())
if K == 0:
    print(0)
    exit()
cats = []
for _ in range(K):
    i, j = map(int, input().split())
    if i > N or j > M:
        continue
    cats.append((i, j))
cats.sort()
# print(cats)
d = [cats[0][1]]
for i in range(1, len(cats)):
    r, c = cats[i]
    idx = bisect_left(d, c)
    # print(idx, c)
    # print(d)
    if c >= d[-1]:
        d.append(c)
    else:
        if d[idx] == c:
            d[bisect_left(d, c + 1)] = c
        d[idx] = c
print(len(d))