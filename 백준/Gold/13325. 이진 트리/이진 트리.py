import sys

sys.setrecursionlimit(2000000)

N = int(input())
weight = [0] * 2 + list(map(int, input().split()))
ans = sum(weight)


def dfs(i):
    global ans
    if i >= 2 ** N:
        return weight[i]
    left = dfs(2 * i)
    right = dfs(2 * i + 1)

    ans += abs(left - right)
    return max(left, right) + weight[i]


dfs(1)
print(ans)
