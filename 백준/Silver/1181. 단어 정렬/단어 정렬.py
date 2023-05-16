N = int(input())
lst = [input() for _ in range(N)]
lst = sorted(list(set(lst)), key= lambda x: (len(x), x))
for i in lst:
    print(i)