import sys

st = input()
K = input()

stk = []

M = len(K)

for ch in st:
    if M - 1 <= len(stk) and (''.join(stk[-M + 1:]) + ch == K or K == ch):
        for _ in range(M - 1):
            stk.pop()
    else:
        stk.append(ch)

if stk:
    print(''.join(stk))
else:
    print('FRULA')