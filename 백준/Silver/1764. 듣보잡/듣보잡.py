N, M = map(int, input().split())

set1 = set(input() for _ in range(N))
set2 = set(input() for _ in range(M))
set3 = set1 & set2
set3 = list(set3)
set3.sort()
print(len(set3), *set3, sep='\n')
