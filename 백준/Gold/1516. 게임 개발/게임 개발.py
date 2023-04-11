import sys

N = int(sys.stdin.readline())
adjl = [[] for _ in range(N)]
times = []
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    M = len(lst)
    for j in lst[1:M - 1]:
        adjl[i].append(j - 1)
    times.append(lst[0])

dp = {}


def dfs(i):
    if not adjl[i]:
        return times[i]
    answer = 0
    if i in dp:
        return dp[i]
    for j in adjl[i]:
        answer = max(answer, dfs(j) + times[i])
    dp[i] = answer
    return answer


for i in range(N):
    print(dfs(i))
