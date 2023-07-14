from collections import defaultdict

def solution(n, results):
    win, lose = defaultdict(set), defaultdict(set)
    
    for winner, loser in results:
        win[loser].add(winner)
        lose[winner].add(loser)
    for i in range(1, n + 1):
        for winner in win[i]:
            win[i] = win[i].union(win[winner])
        for loser in lose[i]:
            lose[i] = lose[i].union(lose[loser])
        for winner in win[i]:
            win[i] = win[i].union(win[winner])
        for loser in lose[i]:
            lose[i] = lose[i].union(lose[loser])
        for winner in win[i]:
            win[i] = win[i].union(win[winner])
        for loser in lose[i]:
            lose[i] = lose[i].union(lose[loser])
        for winner in win[i]:
            win[i] = win[i].union(win[winner])
        for loser in lose[i]:
            lose[i] = lose[i].union(lose[loser])
        for winner in win[i]:
            win[i] = win[i].union(win[winner])
        for loser in lose[i]:
            lose[i] = lose[i].union(lose[loser])
        for winner in win[i]:
            win[i] = win[i].union(win[winner])
        for loser in lose[i]:
            lose[i] = lose[i].union(lose[loser])
        
    
    ans = 0
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            ans += 1
    return ans