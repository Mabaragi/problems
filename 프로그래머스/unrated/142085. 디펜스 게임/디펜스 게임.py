import heapq

def solution(n, k, enemy):
    N = len(enemy)
    heap = []
    num = k
    round = 0
    for i in range(N):
        heapq.heappush(heap, -enemy[i])
        if num > 0 and n < enemy[i]:
            num -= 1
            n += heapq.heappop(heap) * -1
        n -= enemy[i]
        if n < 0:
            break
        round += 1
        
    return round