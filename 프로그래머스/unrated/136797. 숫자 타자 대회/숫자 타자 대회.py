def solution(numbers):
    typings = [(0, 0), (0, 1), (0, 2),
               (1, 0), (1, 1), (1, 2),
               (2, 0), (2, 1), (2, 2),
               (3, 0), (3, 1), (3, 2),]
    positions = {'1': 0, '2': 1, '3': 2, 
                 '4': 3, '5': 4, '6': 5, 
                 '7': 6, '8': 7, '9': 8, 
                 '*': 9, '0': 10, '#': 11,}
    
    N = len(numbers)
    INF = N * 100
    
    def get_cost(current, next):
        if current == next:
            return 1
        x_distance = abs(typings[current][0] - typings[next][0])
        y_distance = abs(typings[current][1] - typings[next][1])                
        return 3 * min(x_distance, y_distance) + 2 * abs(x_distance-y_distance)
    
    dp = [[[INF for _ in range(12)] for _ in range(12)] for _ in range(N + 1)]
    
    dp[0][3][5] = 0
    
    for i in range(0, N):
        number = numbers[i]
        position = positions[number]
        for l in range(12):
            for r in range(12):
                if dp[i][l][r] != INF:
                    if position != r:
                        dp[i + 1][position][r] = min(dp[i + 1][position][r], dp[i][l][r] + get_cost(l, position))
                    if position != l:
                        dp[i + 1][l][position] = min(dp[i + 1][l][position], dp[i][l][r] + get_cost(r, position))
        
    answer = min([min(i) for i in dp[N]])
    return answer