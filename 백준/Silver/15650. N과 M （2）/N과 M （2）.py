import sys

N, M = map(int, input().split())

lst = [i + 1 for i in range(N)]

def func(i, k, st):
    if k == N + 1:
        print(st)
        return
    for r in range(i, k):
        func(r + 1, k + 1, st + str(lst[r]) + ' ')

func(0, N-M + 1, '')