N = int(input())
stair = [int(input()) for _ in range(N)]
memoi = [0] * 300
if N <= 2:
    print(sum(stair[:N]))
else:
    memoi[0] = stair[0]
    memoi[1] = stair[0] + stair[1]
    memoi[2] = max(stair[1] + stair[2], stair[0] + stair[2])

    for i in range(3, N):
        memoi[i] = max(memoi[i - 3] + stair[i - 1] + stair[i], memoi[i - 2] + stair[i])

    print(memoi[N - 1])
