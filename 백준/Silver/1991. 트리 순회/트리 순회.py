def tree1(nod):
    if nod == '.':
        return
    print(nod, end='')
    tree1(l_child[nod])
    tree1(r_child[nod])


def tree2(nod):
    if nod == '.':
        return
    tree2(l_child[nod])
    print(nod, end='')
    tree2(r_child[nod])


def tree3(nod):
    if nod == '.':
        return
    tree3(l_child[nod])
    tree3(r_child[nod])
    print(nod, end='')


N = int(input())

l_child = {}
r_child = {}
for _ in range(N):
    a, b, c = input().split()
    l_child[a] = b
    r_child[a] = c

tree1('A')
print()
tree2('A')
print()
tree3('A')
