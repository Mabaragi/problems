import sys

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

ans = sum([sum(i) for i in array])
array2 = [i[:] for i in array]

for m in range(N):
    for s in range(N):
        if s == m:
            continue
        for e in range(N):
            if e == m:
                continue
            if array2[s][e] > array2[s][m] + array2[m][e]:
                array2[s][e] = array2[s][m] + array2[m][e]
                print(-1)
                exit()
"""
5
0 6 15 2 6
6 0 9 8 12
15 9 0 16 18
2 8 16 0 4
6 12 18 4 0

이미 플로이드가 적용된 상태
"""
for m in range(N):
    for s in range(N):
        if s == m:
            continue
        for e in range(N):
            if e == m:
                continue
            if array[s][e] == array[s][m] + array[m][e]:
                ans -= array[s][e]
                array2[s][e] = 0

print(sum([sum(i) for i in array2]) // 2)


