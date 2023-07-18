def solution(players, callings):
    dct = {}
    N = len(players)
    for i in range(N):
        dct[players[i]] = i
    for calling in callings:
        num = dct[calling]
        dct[calling] -= 1
        dct[players[num - 1]] += 1
        players[num], players[num-1] = players[num - 1], players[num]
        
    return players