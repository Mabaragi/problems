def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        my_set[b] = a
    else:
        my_set[a] = b

def find(a) : # 부모 찾기 연산. 부모 찾을때 부모 업데이트
    root = a
    while root != my_set[root]: #루트 찾기
        root = my_set[root]
    while a != my_set[a]:
        my_set[a] = root
        a = my_set[a]
    return a

N, M = map(int,input().split())
my_set = [i for i in range(N+1)]

for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    if cmd == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')