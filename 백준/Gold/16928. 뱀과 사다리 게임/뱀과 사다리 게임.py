N, M = map(int, input().split())

ladder = {}
snake = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b

memoi = [0] * 101


def func(i, p):
    if p > 100:
        return
    if memoi[p] != 0 and memoi[p] < i:
        return
    memoi[p] = i
    if p in ladder:
        func(i, ladder[p])
        return
    if p in snake:
        func(i, snake[p])
        return
    func(i + 1, p + 6)
    func(i + 1, p + 5)
    func(i + 1, p + 4)
    func(i + 1, p + 3)
    func(i + 1, p + 2)
    func(i + 1, p + 1)


func(0, 1)
print(memoi[100])