T = int(input())
for tc in range(T):
    lst = list(map(int, input().split()))  # 0번은 병사의수, 1 ~ N 번은 병사의 번호
    cnt = {lst[i]: 0 for i in range(1,lst[0]+1)}
    ans = 'SYJKGW'
    for i in range(1, lst[0]+1):
        cnt[lst[i]] += 1
    for i in cnt:
        if 2 * cnt[i] > lst[0]:
            ans = i
    print(ans)