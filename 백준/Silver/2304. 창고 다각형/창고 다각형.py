N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

mx = 0
left_max = 0
for i in lst:
    if mx < i[1]:
        left_max = i[0]
        mx = i[1]
right_max = 0
for i in lst:
    if mx <= i[1]:
        right_max = i[0]

ans = (right_max - left_max + 1) * mx
temp_h = lst[0][1]
temp_p = lst[0][0]
for i in lst:
    if temp_h < i[1]:
        ans += (i[0] - temp_p) * temp_h
        temp_h = i[1]
        temp_p = i[0]
    if i[1] == mx:
        break

temp_h = lst[-1][1]
temp_p = lst[-1][0]
for i in reversed(lst):
    if temp_h < i[1]:
        ans += (-i[0] + temp_p) * temp_h
        temp_h = i[1]
        temp_p = i[0]
    if i[1] == mx:
        break

print(ans)