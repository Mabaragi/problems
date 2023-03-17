"""
크기가 가장 큰 블록 그룹을 찾는다. 
그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 
그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 
그 것도 여러개이면 열이 가장 큰 것을 찾는다.
"""

N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

"""
크기가 가장 큰 블록 그룹을 찾는 함수.
무지개 블록은 중복해서 선택 될 수 있지만, 하나의 그룹에서는 중복 될 수 없음.
까다로운 조건을 맞추기 위해서 tem_blocs 형태의 변수 사용
"""


def find_blocs():
    blocs_cnt = [0, 0]
    blocs = []
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and array[i][j] != 0 and array[i][j] != -1 and array[i][j] != 99:
                qu = [(i, j)]
                visit[i][j] = 1
                tem_blocs = [(i, j)]
                tem_blocs_cnt = [0, 0]
                rainbow_visit = [[0] * N for _ in range(N)]
                while qu:
                    ci, cj = qu.pop(0)
                    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and rainbow_visit[ni][nj] == 0 and (
                                array[ni][nj] == 0 or array[ni][nj] == array[i][j]):
                            qu.append((ni, nj))
                            tem_blocs.append((ni, nj))
                            tem_blocs_cnt[0] += 1
                            if array[ni][nj] != 0:
                                visit[ni][nj] = 1
                            else:
                                tem_blocs_cnt[1] += 1
                                rainbow_visit[ni][nj] = 1

                if blocs_cnt <= tem_blocs_cnt:
                    blocs_cnt = tem_blocs_cnt
                    blocs = tem_blocs
    return blocs


"""
중력을 적용하는 함수.
99이 빈 공간.
아래에서 부터 채워넣자.
"""


def gravity():
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if array[i][j] != 99 and array[i][j] != -1:
                for c in range(i, N - 1):
                    if array[c + 1][j] != 99:
                        array[i][j], array[c][j] = array[c][j], array[i][j]
                        break
                else:
                    array[i][j], array[N - 1][j] = array[N - 1][j], array[i][j]


def rotate():
    global array
    temp_array = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_array[N - 1 - j][i] = array[i][j]
    array = temp_array


ans = 0

while True:
    rem_blocs = find_blocs()
    if len(rem_blocs) < 2:
        break
    for bloc in rem_blocs:
        i, j = bloc
        array[i][j] = 99
    ans += len(rem_blocs) ** 2
    gravity()
    rotate()
    gravity()

print(ans)
