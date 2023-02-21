N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
lst = sorted(lst, key=lambda x: x[1])

stk = [lst[0]]
for i in range(1, N):
    if lst[i][0] >= stk[-1][1]:
        stk.append(lst[i])
print(len(stk))