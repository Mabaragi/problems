N = int(input())

lst = list(map(int, input().split()))
D = lst[:]
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if lst[i] > lst[j]:
            D[i] = max(D[j] + lst[i], D[i])
print(max(D))
