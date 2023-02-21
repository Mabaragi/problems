N = int(input())
pain_lst = list(map(int, input().split()))
joy_lst = list(map(int, input().split()))
"""
i: 깊이. N일때 종료
joy: 기쁨수치. 계속 이어 받으면서 저장
hp: 이어 받으면서 깎음. 0이되면 종료

"""
ans = []
def func(i, joy, hp):
    global ans
    if hp <= 0:
        return
    if i == N:
        ans.append(joy)
        return
    func(i + 1, joy + joy_lst[i], hp - pain_lst[i])  # i 번쨰를 선택하고 넘김
    func(i + 1, joy, hp)  # i번째를 선택하지 않고 넘김

func(0, 0, 100)
print(max(ans))