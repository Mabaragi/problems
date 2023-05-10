from bisect import bisect_left


N = int(input())
lst = list(map(int, input().split()))
D = []
ans_lst = []
for i in range(N):
    idx = bisect_left(D, lst[i])
    if idx >= len(D):
        D.append(lst[i])
    else:
        D[idx] = lst[i]
    ans_lst.append((lst[i], idx))
    
print(len(D))
ans = []
mx_idx = len(D) - 1
for i in range(N - 1, -1, -1):
    val, idx = ans_lst[i]
    if idx == mx_idx:
        ans.append(val)
        mx_idx -= 1

print(*ans[::-1])