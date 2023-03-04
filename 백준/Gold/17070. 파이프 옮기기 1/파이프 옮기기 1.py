N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def pipe(s, hi, hj):  # s 는 상태. 0은 가로, 1은 세로, 2는 대각
    global ans
    if hi == N - 1 and hj == N - 1:
        ans += 1
    if hi + 1 < N and hj + 1 < N and array[hi][hj + 1] != 1 and array[hi + 1][hj] != 1 and array[hi + 1][hj + 1] != 1:
        pipe(2, hi + 1, hj + 1)  # 대각 이동
    if s != 1 and hj + 1 < N and array[hi][hj + 1] != 1:
        pipe(0, hi, hj + 1)  # 가로 이동
    if s != 0 and hi + 1 < N and array[hi+1][hj] != 1:  # 세로로 놓인 상태
        pipe(1, hi + 1, hj)  # 세로 이동


pipe(0, 0, 1)
print(ans)
