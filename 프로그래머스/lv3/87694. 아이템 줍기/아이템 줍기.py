from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    visit = [[0] * 120 for _ in range(101)]
    array = [[0] * 120 for _ in range(101)]

    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        array[y1][x1] = array[y2][x2] = array[y2][x1] = array[y1][x2] = 1
        for i in range(x1 + 1, x2):
            array[y1][i] = array[y2][i] = 1
            visit[y1 + 1][i] = 1
            visit[y2 - 1][i] = 1
        for i in range(y1 + 1, y2):
            array[i][x1] = array[i][x2] = 1
            visit[i][x1 + 1] = 1
            visit[i][x2 - 1] = 1

    qu = deque([(characterY * 2, characterX * 2)])
    visit[characterY * 2][characterX * 2] = 1

    while qu:
        cy, cx = qu.popleft()
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0<=ny<101 and 0<=nx<101 and visit[ny][nx] == 0 and array[ny][nx] == 1:
                visit[ny][nx] = visit[cy][cx] + 1
                qu.append((ny, nx))

    return (visit[itemY * 2][itemX * 2] - 1)//2