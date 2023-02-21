N = int(input())
M = int(input())

adjl = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

stk = []
visit = [0] * (N + 1)
visit[1] = 1
ans = 0
c = 1
while True:
    for i in adjl[c]:
        if visit[i] == 0:
            stk.append(c)
            c = i
            visit[c] = 1
            ans += 1
            break
    else:
        if stk:
            c = stk.pop()
        else:
            break
print(ans)