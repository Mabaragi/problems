N = int(input())

o_sugar = N
five_sugar = 0
three_sugar = 0
five_sugar += N // 5
o_sugar = o_sugar % 5
ans = -1
while o_sugar <= N:
    if o_sugar % 3 == 0:
        three_sugar = o_sugar // 3
        ans = five_sugar + three_sugar
        break
    five_sugar -= 1
    o_sugar += 5
print(ans)