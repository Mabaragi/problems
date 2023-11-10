import collections
import sys


K = int(sys.stdin.readline())
N, M = map(int, sys.stdin.readline().split())
pizza_a = [int(sys.stdin.readline()) for _ in range(N)] * 2
pizza_b = [int(sys.stdin.readline()) for _ in range(M)] * 2

for i in range(1, 2 * N):
    pizza_a[i] += pizza_a[i - 1]
for i in range(1, 2 * M):
    pizza_b[i] += pizza_b[i - 1]
cache_a = collections.defaultdict(int)
cache_b = collections.defaultdict(int)
cache_a[0] = 1
cache_a[pizza_a[N - 1]] = 1
cache_b[0] = 1
cache_b[pizza_b[M - 1]] = 1
for i in range(N):
    for j in range(i + 1, i + N):
        cache_a[pizza_a[j] - pizza_a[i]] += 1
for i in range(M):
    for j in range(i + 1, i + M):
        cache_b[pizza_b[j] - pizza_b[i]] += 1
answer = 0
for i in range(K + 1):
    answer += cache_a[i] * cache_b[K-i]

print(answer)