def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    drc = [(1, 0), (0, 1), (-1, -1)]  # 방향: 아래, 오른쪽, 왼쪽 위 대각선
    d = 0  # 초기 방향
    x, y = 0, 0  # 초기 좌표
    cnt = 1
    for i in range(n * (n + 1) // 2):  # 채울 숫자의 총 합
        answer[x][y] = cnt
        nx, ny = x + drc[d][0], y + drc[d][1]
        
        # 범위를 벗어나거나 이미 숫자가 채워진 칸이라면 방향을 바꿈
        if nx >= n or ny >= len(answer[nx]) or answer[nx][ny] != 0:
            d = (d + 1) % 3
            nx, ny = x + drc[d][0], y + drc[d][1]
            
        x, y = nx, ny
        cnt += 1
    lst = []
    for i in answer:
        lst += i
        
    return lst