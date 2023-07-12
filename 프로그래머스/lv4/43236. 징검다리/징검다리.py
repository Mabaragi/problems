def solution(distance, rocks, n):
    left, right = 0, distance
    rocks.sort()
    rocks += [distance]
    
    while left <= right:        
        limit = 0
        pre_rock = 0
        mid = (left + right) // 2
        for rock in rocks:
            if mid > rock - pre_rock:
                limit += 1
            else:
                pre_rock = rock
        if limit > n:
            right = mid - 1
        else:
            ans = mid
            left = mid + 1
    return ans