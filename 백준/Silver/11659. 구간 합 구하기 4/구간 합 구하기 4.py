import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sms = [0]
sm = 0
for i in nums:
    sm += i
    sms.append(sm)
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(sms[e] - sms[s-1])