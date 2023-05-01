import sys
from collections import deque

"""
1. 자료 읽기.
2 로 나눈 나머지가 1보다 크거나 같으면 서쪽벽 = 2로 나눈 나머지가 1보다 작으면 서쪽으로 갈 수 있음
4로 나눈 나머지가 2보다 크거나 같으면 북쪽벽 = 4로 나눈 나머지가 2보다 작으면 북쪽으로 갈 수 있음
8로 나눈 나머지가 4보다 크거나 같으면 동쪽벽 ...
8보다 크거나 같은 수면 남쪽벽

2. 방의개수, 가장 넓은 방의 크기
visit에 두개의 변수를 받는다 (방번호, 방크기)

3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
인접한 방의 번호를 
"""

N, M = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

visit = [[0] * N for _ in range(M)]

mx_rooms_number = 0

dct = {}
room_number = 0
for i in range(M):
    for j in range(N):
        if visit[i][j] == 0:
            rooms_number = 1
            qu = deque([(i, j)])
            # 방의 좌표를 담을 배열
            literals =[(i, j)]
            visit[i][j] = (room_number, rooms_number)

            while qu:
                ci, cj = qu.popleft()
                if array[ci][cj] % 2 == 0 and cj - 1 >= 0 and visit[ci][cj - 1] == 0:  # 서쪽으로 갈 수 있으면
                    rooms_number += 1  # 방 개수 증가
                    visit[ci][cj - 1] = (room_number, rooms_number)
                    qu.append((ci, cj - 1))
                    literals.append((ci, cj - 1))
                if array[ci][cj] % 4 < 2 and ci - 1 >= 0 and visit[ci - 1][cj] == 0:
                    rooms_number += 1
                    visit[ci - 1][cj] = (room_number, rooms_number)
                    qu.append((ci - 1, cj))
                    literals.append((ci - 1, cj))
                if array[ci][cj] % 8 < 4 and cj + 1 < N and visit[ci][cj + 1] == 0:
                    rooms_number += 1
                    visit[ci][cj + 1] = (room_number, rooms_number)
                    qu.append((ci, cj + 1))
                    literals.append((ci, cj + 1))
                if array[ci][cj] < 8 and ci + 1 < M and visit[ci + 1][cj] == 0:
                    rooms_number += 1
                    visit[ci + 1][cj] = (room_number, rooms_number)
                    qu.append((ci + 1, cj))
                    literals.append((ci + 1, cj))
            # 방 크기 최대값 갱신
            if mx_rooms_number < rooms_number:
                mx_rooms_number = rooms_number
            # 방 번호 증가
            for li, lj in literals:
                dct[li, lj] = (room_number, rooms_number)

            room_number += 1

print(room_number)
print(mx_rooms_number)
mx = 0
for i, j in dct:
    room_number, rooms_number = dct[i, j]
    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ni, nj = i + di, j + dj
        if (ni, nj) in dct:
            other_room_number, other_rooms_number = dct[ni,nj]
            if room_number != other_room_number and rooms_number + other_rooms_number > mx:
                mx = rooms_number + other_rooms_number

print(mx)