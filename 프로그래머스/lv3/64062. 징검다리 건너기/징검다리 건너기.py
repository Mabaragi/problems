def solution(stones, k):
    left, right = 0, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        streak = 0
        for stone in stones:
            if stone < mid:
                streak += 1
                if streak == k:
                    break        
            else:
                streak = 0
        else:
            answer = mid
            left = mid + 1    
            continue
        right = mid - 1

    return answer