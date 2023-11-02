N = int(input())
lst = list(map(int, input().split()))
M = int(input())
for i in range(N - 1):
    # 최대값 탐색
    mx, idx = lst[i], i
    for j in range(i + 1, min(i + M + 1, N)):
        if mx < lst[j]:
            mx, idx = lst[j], j
    M -= idx - i
    for j in range(idx - 1, i - 1, -1):
        lst[j + 1] = lst[j]
    lst[i] = mx
print(*lst)