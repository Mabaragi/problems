"""
상점 방향 - 동근이 방향 
-1 or 3: 왼쪽
-2 or 2: 맞은편
1 or -3 : 오른쪽
0 : 같은 방향
    1    
2       4
    3

"""

r, c = map(int, input().split())  # r: 가로길이, c: 세로 길이
N = int(input())  # 상점의 개수
shops = []
bang = {1: 1, 2: 3, 3: 2, 4: 4}
for i in range(N):
    shops.append(list(map(int, input().split())))
for i in range(N):
    shops[i][0] = bang[shops[i][0]]
me = list(map(int, input().split()))
me[0] = bang[me[0]]
"""
튜플에서 0은 방향정보, 1은 위치 정보
동근이의 방향의 경우를 나누어 생각해 보자
"""
D = 0
if me[0] == 3:  # 동근이가 남쪽일 경우
    for shop in shops:
        if shop[0] - me[0] == -1 or shop[0] - me[0] == 3:  # 왼쪽일 경우
            D += me[1] + c - shop[1]
        elif shop[0] - me[0] == -2 or shop[0] - me[0] == 2:  # 맞은편 일 경우
            D += min([c + me[1] + shop[1], c + 2 * r - me[1] - shop[1]])
        elif shop[0] - me[0] == 1 or shop[0] - me[0] == -3:  # 오른쪽 일 경우
            D += r - me[1] + c - shop[1]
        else:
            D += abs(shop[1] - me[1])
elif me[0] == 1:  # 동근이가 북쪽일 경우
    for shop in shops:
        if shop[0] - me[0] == 1 or shop[0] - me[0] == -3:  # 오른쪽일 경우
            D += me[1] + shop[1]
        elif shop[0] - me[0] == -2 or shop[0] - me[0] == 2:  # 맞은편 일 경우
            D += min([c + me[1] + shop[1], c + 2 * r - me[1] - shop[1]])
        elif shop[0] - me[0] == -1 or shop[0] - me[0] == 3:  # 왼쪽 일 경우
            D += r - me[1] + shop[1]
        else:
            D += abs(shop[1] - me[1])
elif me[0] == 2:  # 동근이가 서쪽일 경우
    for shop in shops:
        if shop[0] - me[0] == 1 or shop[0] - me[0] == -3:  # 오른쪽일 경우
            D += c - me[1] + shop[1]
        elif shop[0] - me[0] == -2 or shop[0] - me[0] == 2:  # 맞은편 일 경우
            D += min([r + me[1] + shop[1], r + 2 * c - me[1] - shop[1]])
        elif shop[0] - me[0] == -1 or shop[0] - me[0] == 3:  # 왼쪽 일 경우
            D += me[1] + shop[1]
        else:
            D += abs(shop[1] - me[1])
elif me[0] == 4:  # 동근이가 동쪽일 경우
    for shop in shops:
        if shop[0] - me[0] == 1 or shop[0] - me[0] == -3:  # 오른쪽일 경우
            D += me[1] + r - shop[1]
        elif shop[0] - me[0] == -2 or shop[0] - me[0] == 2:  # 맞은편 일 경우
            D += min([r + me[1] + shop[1], r + 2 * c - me[1] - shop[1]])
        elif shop[0] - me[0] == -1 or shop[0] - me[0] == 3:  # 왼쪽 일 경우
            D += c - me[1] + r - shop[1]
        else:
            D += abs(shop[1] - me[1])
print(D)
