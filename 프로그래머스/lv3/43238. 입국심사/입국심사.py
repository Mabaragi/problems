import bisect

def solution(n, times):
    left, right = 0, times[-1] * n
    while left < right:
        target = (left + right)//2
        val = 0
        for time in times:
            val += target // time
        
        if val >= n:
            ans = target
            right = target
        else:
            left = target + 1            
    return ans