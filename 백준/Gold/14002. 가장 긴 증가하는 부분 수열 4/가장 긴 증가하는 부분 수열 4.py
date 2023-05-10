from bisect import bisect_left


N = int(input())
lst = list(map(int, input().split()))
D = []
DP = [[] for _ in range(N + 1)]
for i in range(N):
    idx = bisect_left(D, lst[i])
    if idx >= len(D):
        D.append(lst[i])
    else:
        D[idx] = lst[i]
    DP[idx + 1] = DP[idx] + [lst[i]]
print(len(D))
print(*DP[len(D)])