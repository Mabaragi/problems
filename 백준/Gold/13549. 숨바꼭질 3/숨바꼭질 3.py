import sys

N, K = map(int, sys.stdin.readline().split())

qu = [(N, 0)]

visit = [100000] * 100001
visit[N] = 0

while qu:
    cn, ci = qu.pop(0)
    for nn, ni in ((cn - 1, ci + 1), (cn + 1, ci + 1), (2 * cn, ci)):
        if (0 <= nn < 100001) and visit[nn] > ni:
            qu.append((nn, ni))
            visit[nn] = ni
print(visit[K])
