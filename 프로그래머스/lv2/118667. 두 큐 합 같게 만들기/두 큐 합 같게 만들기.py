def solution(queue1, queue2):
    N = len(queue1)
    M = len(queue2)

    lst = queue1 + queue2
    K = sum(lst) // 2
    i, j = 0, N
    j_cnt = 0
    ans = -1
    cnt = 0
    num = sum(queue1)
    while j_cnt < N + M:
        if num == K:
            ans = cnt
            break
        if num > K:
            num -= lst[i]
            i = (i + 1) % (N + M)
        elif num < K:
            num += lst[j]
            j_cnt += 1
            j = (j + 1) % (N + M)
        cnt += 1
    return ans