N = int(input())
M = int(input())
left = 1
right = N**2

while left <= right:
    middle = (left + right) // 2
    # middle 보다 작은 수의 개수 새기
    num = 0
    for i in range(1, N + 1):
        # 각 행 별로 num보다 작거나 같은 수의 개수 더하기
        num += min(N, middle//i)
    # num이 M보다 작으면 답의 가능성이 없음. middle의 숫자 키위서 다시 탐색
    if num < M:
        left = middle + 1
    # num 이 M보다 크면 답의 가능성이 있음. middle 숫자 작게해서 탐색
    else:
        right = middle - 1
        ans = middle

print(ans)