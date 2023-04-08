def solution(line):
    N = len(line)
    stars = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            A, B, E = line[i]
            C, D, F = line[j]
            if A * D == B * C:
                continue
            M = A * D - B * C
            x = B * F - E * D
            y = E * C - A * F
            if x % M or y % M:
                continue
            stars.append((x // M, y // M))

    max_x, min_x, max_y, min_y = max(i[0] for i in stars), min(i[0] for i in stars), max(i[1] for i in stars), min(
        i[1] for i in stars)
    answer = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for x, y in stars:
        i = y * - 1 + max_y
        j = x - min_x
        answer[i][j] = '*'

    for i in range(max_y - min_y + 1):
        answer[i] = ''.join(answer[i])
    return answer