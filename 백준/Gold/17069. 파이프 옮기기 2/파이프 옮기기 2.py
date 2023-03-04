N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
dp1 = [[0] * N for _ in range(N)]  # 가로인 상태의 경우의 수
dp2 = [[0] * N for _ in range(N)]  # 세로인 상태의 경우의 수
dp3 = [[0] * N for _ in range(N)]  # 대각선 상태의 경우의 수
dp1[0][1] = 1  # 초기에 0,1 에 가로 상태로 놓임
for j in range(2, N):
    if array[0][j] == 0:
        dp1[0][j] = dp1[0][j - 1]

for i in range(1, N):
    for j in range(1, N):
        if array[i][j] == 0 and array[i-1][j] == 0 and array[i][j-1] == 0:
            dp3[i][j] = dp3[i - 1][j - 1] + dp1[i - 1][j - 1] + dp2[i - 1][j - 1]
        if array[i][j] == 0:
            dp1[i][j] = dp3[i][j - 1] + dp1[i][j - 1]
            dp2[i][j] = dp3[i-1][j] + dp2[i-1][j]

print(dp1[N-1][N-1] + dp2[N-1][N-1] + dp3[N-1][N-1])
