def func():
    i = 0
    for _ in range(K):
        change, alpha = input().split()
        change = int(change)
        i = (i + change) % N
        if lst[i] != '?' and lst[i] != alpha or alpha in lst and lst[i] != alpha:
            print('!')
            return
        lst[i] = alpha
    print(''.join(lst[i::-1] + lst[:i:-1]))
    return


N, K = map(int, input().split())
lst = ['?'] * N
func()
