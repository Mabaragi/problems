from bisect import bisect_left, bisect_right

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A_sum = []
for i in range(N):
    A_sum.append(A[i])
    for j in range(i + 1, N):
        A_sum.append(A_sum[-1] + A[j])
B_sum = []
for i in range(M):
    B_sum.append(B[i])
    for j in range(i + 1, M):
        B_sum.append(B_sum[-1] + B[j])
A_sum.sort()
B_sum.sort()
result = 0
for i in range(len(A_sum)):
    l = bisect_left(B_sum, T - A_sum[i])
    r = bisect_right(B_sum, T - A_sum[i])
    result += r - l

print(result)