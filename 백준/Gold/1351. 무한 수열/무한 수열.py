import math
import collections


N, P, Q = map(int, input().split())

precomp = collections.defaultdict(int)
precomp[0] = 1
def get_An(N):
    if precomp[N] == 0:
        precomp[N] = get_An(math.floor(N/Q)) + get_An(math.floor(N/P))
    return precomp[N]

print(get_An(N))