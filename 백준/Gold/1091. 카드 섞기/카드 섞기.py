N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

cards = [i for i in range(N)]
cnt = 0

# 세명의 플레이어가 올바른 카드를 받을 때 까지.
while P != [cards[i] % 3 for i in range(N)]:
    # 카드를 주어진 규칙에 따라 셔플
    cards = [S[cards[i]] for i in range(N)]
    cnt += 1
    # 카드가 초기상태랑 같음 = 무한루프 된다는 뜻
    if cards == [i for i in range(N)]:
        cnt = -1
        break
print(cnt)