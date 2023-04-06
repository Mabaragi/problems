def func(num):
    if num == -1:
        return 0
    num = bin(num)
    l = len(num)
    counts = 0
    tem = 0
    for i in range(l - 1, 1, -1):
        idx = l - i - 1
        if num[i] == '1':
            counts += int(2 ** (idx - 1)) * idx + 1 + tem
            tem += 2 ** idx
    return counts

N, M = map(int, input().split())
print(func(M) - func(N - 1))