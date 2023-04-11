import sys

sys.setrecursionlimit(200000)
N = int(sys.stdin.readline())
adjl = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    adjl[a].append(b)
weights = list(map(int, sys.stdin.readline().split()))


def func(i):
    if not adjl[i]:
        return max(0, weights[i])
    ans = 0
    for j in adjl[i]:
        ans += func(j)
    return max(0, ans + weights[i])


ans = 0
for j in adjl[0]:
    ans += func(j)
ans += weights[0]
print(ans)