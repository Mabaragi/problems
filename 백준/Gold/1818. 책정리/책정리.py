from bisect import bisect_left

N = int(input())
lst = list(map(int, input().split()))

d = []

for i in range(N):
    idx = bisect_left(d, lst[i])
    if idx >= len(d):
        d.append(lst[i])
    else:
        d[idx] = lst[i]

print(N - len(d))