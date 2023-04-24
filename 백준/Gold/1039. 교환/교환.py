from collections import deque

st, K = input().split()
K = int(K)
N = len(st)

qu = deque([(st, 0)])
ans = -1
visit = set()
while qu:
    num, cnt = qu.popleft()
    if cnt == K:
        num = int(num)
        if ans < num:
            ans = num
        continue
    array = list(num)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if i == 0 and array[j] == '0': continue
            array[i], array[j] = array[j], array[i]
            next_num = ''.join(array)
            if (next_num, cnt + 1) not in visit:
                qu.append((next_num, cnt + 1))
                visit.add((next_num, cnt + 1))
            array[i], array[j] = array[j], array[i]

print(ans)