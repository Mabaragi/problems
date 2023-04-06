T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    ans = [[0] * (N + 1) for _ in range(N + 1)]
    
    for length in range(2, N + 1):
        for start in range(1, N - length + 2):
            end = start + length - 1
            if length == 2:
                dp[start][end] = lst[start] + lst[end]
            else:
                candidate_1 = dp[start + 1][end] + sum(lst[i] for i in range(start, end + 1))
                candidate_2 = dp[start][end - 1] + sum(lst[i] for i in range(start, end + 1))
                if length == 3:
                    dp[start][end] = min(candidate_1, candidate_2)
                else:
                    candidate_3 = min(
                        [dp[start][middle] + dp[middle + 1][end] for middle in range(start + 1, end - 1)]) + sum(
                        lst[i] for i in range(start, end + 1))
                    dp[start][end] = min(candidate_1, candidate_2, candidate_3)
    print(dp[1][-1])