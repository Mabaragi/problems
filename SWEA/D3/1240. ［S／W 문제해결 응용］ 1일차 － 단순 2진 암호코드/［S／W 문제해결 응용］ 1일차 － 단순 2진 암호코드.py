# 암호를 숫자로 전환하기 위한 딕셔너리
dic = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4, (1, 2, 3, 1): 5,
       (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8, (3, 1, 1, 2): 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    array = [input() for _ in range(N)]
    
    # 암호코드를 탐색함. 열 정보, 암호코드의 가장 끝자리 정보를 가져옴.
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if array[i][j] == '1':
                key = j
                row = i
                break
    code = array[row]
    i = key - 55
    lst = []

    # 암호를 숫자로 전환하기 위해 튜플로 표현
    for t in range(8):
        temp = []
        cnt = 1
        for j in range(i + 7 * t, i + 7 * t + 6):
            if code[j] != code[j + 1]:
                temp.append(cnt)
                cnt = 1
            else:
                cnt += 1
        temp.append(cnt)
        lst.append(tuple(temp))
        
    # 딕셔너리를 이용해 암호를 숫자로 전환 한 뒤에 정답 출력
    c1 = 0
    c2 = 0
    for i in range(0, 8, 2):
        c1 += dic[lst[i]]

    for i in range(1, 8, 2):
        c2 += dic[lst[i]]
    if (c1 * 3 + c2) % 10:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', c1 + c2)
