N = int(input())
lst = list(map(int, input().split()))
if N < 3:
    if N == 2 and lst[0] == lst[1]:
        print(lst[0])
    else:
        print('A')
    exit()
    
if lst[1] == lst[0]:
    a = 1
else:
    a = (lst[2] - lst[1]) // (lst[1] - lst[0])
b = lst[1] - a * lst[0]
for i in range(N - 1):
    if lst[i + 1] != lst[i] * a + b:
        print('B')
        exit()

print(lst[-1] * a + b)
