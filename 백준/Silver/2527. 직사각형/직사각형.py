for tc in range(1, 5):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())

    if a2 < a3 or b2 < b3 or a4 < a1 or b4 < b1:
        print('d')
    elif (a2 == a3 and b1 == b4) or (a2 == a3 and b2 == b3) or (a1 == a4 and b1 == b4) or (a1 == a4 and b2 == b3):
        print('c')
    elif a2 == a3 or a1 == a4 or b1 == b4 or b2 == b3:
        print('b')
    else:
        print('a')
