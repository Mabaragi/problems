N = int(input())

a, b, c = map(int, input().split())
mx1 = mn1 = a
mx2 = mn2 = b
mx3 = mn3 = c
for _ in range(1, N):
    a, b, c = map(int, input().split())
    mx1, mx2, mx3 = max(mx2, mx1) + a, max(mx1, mx2, mx3) + b, max(mx3, mx2) + c
    mn1, mn2, mn3 = min(mn2, mn1) + a, min(mn1, mn2, mn3) + b, min(mn3, mn2) + c
print(max(mx1, mx2, mx3), min(mn1, mn2, mn3))