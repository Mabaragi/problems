import math
import collections


N, P, Q = map(int, input().split())

precomp = collections.defaultdict(int)
def get_An(N):
    if N == 0:
        return 1
    if precomp[N] == 0:
        precomp[N] = get_An(math.floor(N/Q)) + get_An(math.floor(N/P))
    return precomp[N]

print(get_An(N))