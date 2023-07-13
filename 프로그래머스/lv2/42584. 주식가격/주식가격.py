def solution(prices):
    counter = 0
    stk = []
    N = len(prices)
    ans = [N - 1 - i for i in range(N)]
    k = 0
    for i in range(N):
        while stk and stk[-1][0] > prices[i]:  # 비어있으면 제거를 하지 않음
            ans[stk[-1][1]] = i - stk[-1][1]
            stk.pop()
        stk.append([prices[i], i])
        
        

        
    return ans