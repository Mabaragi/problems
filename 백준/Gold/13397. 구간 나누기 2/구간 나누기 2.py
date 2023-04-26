import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(lst) - min(lst)
while left <= right:
    middle = (left + right) // 2
    mn = lst[0]
    mx = lst[0]
    num = 1  # 구간의 수
    for i in range(1, N):
        if mn > lst[i]:
            mn = lst[i]
        if mx < lst[i]:
            mx = lst[i]
        if mx - mn > middle:  # 정해놓은 최댓값의 차이보다 더 크면
            num += 1  # 구간의 개수 증가
            mn = lst[i]
            mx = lst[i]
    if num > M:  # 구간의 개수보다 M 보다 크면 범위를 늘림
        left = middle + 1
    else:
        right = middle - 1
        ans = middle
print(ans)