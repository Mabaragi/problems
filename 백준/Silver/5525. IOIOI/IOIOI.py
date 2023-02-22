N = int(input())
M = int(input())
st = input()

i = 0
ans = 0
while i < M:
    if st[i] == 'I':
        i += 1
        cnt = 0
        while i < M:
            if st[i] != st[i - 1]:
                cnt += 1
            else:
                if cnt >= 2 * N:
                    ans += (2 + cnt - 2 * N) // 2
                i -= 1
                break
            i += 1
    i += 1
if cnt >= 2 * N:
    ans += (2 + cnt - 2 * N) // 2
print(ans)