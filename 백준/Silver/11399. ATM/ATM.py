N = int(input())
lst = list(map(int, input().split()))
lst.sort()
for i in range(1, N):
    lst[i] = lst[i] + lst[i-1]
for i in range(1, N):
    lst[i] = lst[i] + lst[i-1]
print(lst[-1])