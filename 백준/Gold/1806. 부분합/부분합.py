from collections import deque
N, S = map(int, input().split())
series = list(map(int, input().split()))
stk = deque([series[0]])
mn = 100001
sm = series[0]
if sm >= S:
    print(1)
    exit()
for i in range(1, N):
    stk.append(series[i])
    sm += series[i]
    while stk and sm - stk[0] >= S:
        sm -= stk.popleft()
    if sm >= S and mn > len(stk):
        mn = len(stk)
if mn == 100001:
    mn = 0
print(mn)