N = int(input())
train = list(map(int, input().split()))
length = int(input())
dp = [[0] * (N - length + 1) for _ in range(3)]
for first_start in range(N - length * 3 + 1):
    first_end = first_start + length - 1
    dp[0][first_start] = sum(train[first_start:first_end + 1])
for second_start in range(length, N - length * 2 + 1):
    second_end = second_start + length - 1
    dp[1][second_start] = max(dp[0][:second_start - length + 1]) + sum(train[second_start:second_end + 1])
for third_start in range(2 * length, N - length + 1):
    third_end = third_start + length - 1
    dp[2][third_start] = max(dp[1][:third_start - length + 1]) + sum(train[third_start:third_end + 1])

print(max(dp[2]))
