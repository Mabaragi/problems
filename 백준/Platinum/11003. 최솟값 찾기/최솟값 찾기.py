from collections import defaultdict, deque
import sys

N, M =  map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
qu = deque()
qu.append((lst[0], 0))
answer = [lst[0]]
for i in range(1, N):
    if qu[0][1] <= i - M:
        qu.popleft()
    curr = (lst[i], i)
    # if curr[0] <= qu[-1][0]:
    while qu and curr[0] <= qu[-1][0]:
        qu.pop()
    qu.append(curr)
    answer.append(qu[0][0])
print(*answer)