def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0
    
    mn_length = 10e6
    for i in range(n):
        
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1
        
        if max_sum == k and mn_length > end - 1 - i:            
            mn_length = end - 1 - i
            res = [i, end - 1]
        
        max_sum -= sequence[i]
    return res