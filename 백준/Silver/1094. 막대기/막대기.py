N = int(input())

num = 64
remainder = 0
cnt = 1
while num + remainder != N:
    # 합이 x보다 크면 길이가 가장 짧은것을 반으로 자른다
    if num + remainder >= N:
        num //= 2
    if num + remainder < N:
        remainder += num
        cnt += 1

print(cnt)