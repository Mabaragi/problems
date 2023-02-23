import sys

N = int(sys.stdin.readline())
s = 0b0

for i in range(N):
    cmd = list(sys.stdin.readline().split())
    if len(cmd) == 2:
        n = int(cmd[1])
        cmd = cmd[0]
    else:
        cmd = cmd[0]

    if cmd == 'add':
        s = s | (1 << n)
    elif cmd == 'remove':
        s = s & ~(1 << n)
    elif cmd == 'check':
        if s & (1 << n):
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        s = s ^ (1 << n)
    elif cmd == 'all':
        s = (1 << 21) -1
    else:
        s = 0b0