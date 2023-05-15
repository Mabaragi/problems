from collections import deque
from itertools import permutations

N = int(input())
lst = list(map(int, input().split()))

qu = deque([lst])
visit = {}
visit[tuple(lst)] = 0

while qu:
    curr = qu.popleft()
    if sum(curr) == 0:
        print(visit[tuple(curr)])
        break
    for nums in permutations([i for i in range(N)], N):
        next_lst = [max(curr[nums[i]] - 3 ** (2 - i), 0) for i in range(N)]
        if tuple(next_lst) not in visit:
            qu.append(next_lst)
            visit[tuple(next_lst)] = visit[tuple(curr)] + 1
