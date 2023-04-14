def solution(matrix_sizes):
    matrixes = matrix_sizes
    N = len(matrixes)
    dp = [[0] * N for _ in range(N - 1)]
    
    
    for length in range(2, N + 1):
        for start in range(0, N - length + 1):
            end = start + length - 1
            if length == 2:
                dp[start][end] = matrixes[start][0] * matrixes[end][1] * matrixes[start][1]
                continue
            candidate1 = dp[start+1][end] + matrixes[start][0] * matrixes[start][1] * matrixes[end][1]
            candidate2 = dp[start][end - 1] + matrixes[start][0] * matrixes[end][0] * matrixes[end][1]
            if length == 3:
                dp[start][end] = min(candidate1, candidate2)
            else:
                candidate3 = min(dp[start][start + j] + dp[start + j + 1][end] + matrixes[start][0] * matrixes[start + j][1] * matrixes[end][1] for j in range(1, length - 2))
                dp[start][end] = min(candidate1, candidate2, candidate3)    

    answer = dp[0][-1]
    return answer