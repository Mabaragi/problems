def solution(targets):
    N = len(targets)
    targets.sort()
    last = targets[0][-1]
    ans = 1
    for i in range(1, N):
        start, end = targets[i]
        if start >= last:
            last = end
            ans += 1
        elif end < last:
            last = end
    return ans