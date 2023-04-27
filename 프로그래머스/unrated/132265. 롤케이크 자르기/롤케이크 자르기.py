def solution(topping):
    N = len(topping)
    left_visit = {topping[0]}
    right_visit = {topping[-1]}
    left = [0] * N
    left[0] = 1
    right = [0] * N
    right[-1] = 1
    for i in range(1, N):
        if topping[i] not in left_visit:
            left_visit.add(topping[i])
            left[i] = left[i - 1] + 1
        else:
            left[i] = left[i - 1]
        if topping[-i - 1]not in right_visit:
            right_visit.add(topping[-i - 1])
            right[-i - 1] = right[-i] + 1
        else:
            right[-i - 1] = right[-i]
    answer = 0
    for i in range(N - 1):
        if left[i] == right[i + 1]:
            answer += 1
    
    return answer