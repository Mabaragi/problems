import sys

N = int(input())
costs = list(map(int, input().split()))
M = int(input())
lst = [(costs[N - 1], N - 1)]
for i in range(N - 2, - 1, - 1):
    if lst[-1][0] <= costs[i]:
        continue
    lst.append((costs[i], i))

if lst[-1][1] == 0 and len(lst) >= 2:
    max_length = (M - lst[-2][0])//lst[-1][0] + 1
else:
    max_length = M//lst[-1][0]

dp = {}

mx = 0
def function(number, total, length):
    global mx
    # print(dp)
    if number in dp and dp[number] >= total:
        return
    if total > M:
        return
    if length + (M - total)//lst[-1][0] < max_length:
        return
    mx = number
    dp[number] = total
    for i in range(len(lst)):
        function(number + str(lst[i][1]), total + lst[i][0], length + 1)


for i in range(len(lst)):
    if lst[i][1] == 0:
        continue
    function(str(lst[i][1]), lst[i][0], 1)

if dp:
    print(max(map(int, dp.keys())))
else:
    print(0)
