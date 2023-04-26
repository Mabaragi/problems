import sys
N, M, L = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
left = 1
right = L - 1
while left <= right:
    middle = (left + right) // 2
    current = 0
    i = 0
    num = -1
    while current < L:
        # 정한 범위 내에 휴게소가 없으면 휴게소 설치
        if i >= N or current + middle < lst[i]:
            current += middle
            num += 1
        elif i < N:
            current = lst[i]
            i += 1
    # 정해진 개수보다 휴게소 많이 설치하면 범위 늘리기
    if num > M:
        left = middle + 1
    # 같거나 적게 설치했으면 범위 좁히면서 답 탐색
    else:
        right = middle - 1
        ans = middle
print(ans)
