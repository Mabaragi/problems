N = int(input())

lst = list(map(int, input().split()))
D = [1] * N
INF = 1e8
A = [1e8] * N

mx = 0
for i in range(0, N):
    left = 0
    right = len(A) - 1
    ans = - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] >= lst[i]:
            right = mid - 1
        else:
            left = mid + 1
            ans = mid
    A[ans + 1] = lst[i]
    mx = max(mx, ans + 2)
print(mx)