import sys

N, M = map(int, sys.stdin.readline().split())
times = [int(sys.stdin.readline()) for _ in range(N)]
times.sort()
left = 1
right = M * times[-1]

while left <= right:
    middle = (left + right) // 2
    people_num = 0
    for time in times:
        people_num += middle//time
    if people_num < M:
        left = middle + 1
    else:
        right = middle - 1
        ans = middle
print(ans)