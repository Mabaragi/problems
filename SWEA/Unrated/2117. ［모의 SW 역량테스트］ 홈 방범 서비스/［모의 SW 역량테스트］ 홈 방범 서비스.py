# 범위가 K 일때 가장 많은 집의 수를 구하는 함수
def get_houses(K):
    mx = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for r in range(-K + 1, K):
                for c in range(-K + 1, K):
                    if 0 <= i + r < N and 0 <= j + c < N and -K < r + c < K and -K < c - r < K and map1[i + r][
                        j + c] == 1:
                        cnt += 1
            if mx < cnt:
                mx = cnt
    return mx


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    map1 = [list(map(int, input().split())) for _ in range(N)]

    # 가장 넓은 범위부터 좁혀가면서 손해 안보는 시점을 찾음
    for K in range(N // 2 * 2 + 1, 0, -1):
        if K * K + (K - 1) * (K - 1) <= get_houses(K) * M:
            print(f'#{tc}', get_houses(K))
            break
