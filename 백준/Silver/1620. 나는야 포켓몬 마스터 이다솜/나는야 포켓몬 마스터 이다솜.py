N, M = map(int, input().split())
dic = {}
dic2 = {}
for i in range(1, N + 1):
    poke = input()
    dic[poke] = i
    dic2[i] = poke

for _ in range(M):
    k = input()
    if k.isdigit():
        print(dic2[int(k)])
    else:
        print(dic[k])