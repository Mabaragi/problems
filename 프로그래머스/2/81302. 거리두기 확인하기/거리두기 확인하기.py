from collections import deque

def check(i, j, place):
    visit = [[0] * 5 for _ in range(5)]
    visit[i][j] = 1
    qu = deque([(i,j, 0)])
    while qu:
        ci, cj, d = qu.popleft()
        if d > 1:  # 거리가 2 초과하면 탐색 그만 
            continue
        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] != 'X' and visit[ni][nj] == 0:
                if place[ni][nj] == 'P':  # 만약에 사람이면 False를 return
                    return True
                visit[ni][nj] = 1
                qu.append((ni, nj, d + 1)) 
    return False  # 전부 탐색해도 P를 못만나면 True를 리턴
                

def solution(places):
    answer = [1] * 5
    
    for k in range(5):
        place = places[k]
        flag = False
        for i in range(5):
            if flag:
                break
            for j in range(5):
                if place[i][j] == 'P':
                    if check(i, j, place):
                        answer[k] = 0
                        flag = True
                        break

    return answer