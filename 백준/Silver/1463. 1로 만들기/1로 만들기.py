N = int(input())
memoi = [0] * 1000001
for i in range(2, N + 1):
    if i % 6 == 0:
        memoi[i] = min([memoi[i // 3], memoi[i // 2], memoi[i - 1]]) + 1
    elif i % 3 == 0:
        memoi[i] = min([memoi[i // 3], memoi[i - 1]]) + 1
    elif i % 2 == 0:
        memoi[i] = min([memoi[i // 2], memoi[i - 1]]) + 1
    else:
        memoi[i] = memoi[i - 1] + 1
print(memoi[N])