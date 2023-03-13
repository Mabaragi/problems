import sys

N = int(sys.stdin.readline())

x1, y1 = map(int, sys.stdin.readline().split())
xn, yn = x1, y1

a1 = 0
a2 = 0

for _ in range(N - 1):
    x2, y2 = map(int, sys.stdin.readline().split())
    a1 += x1 * y2
    a2 += x2 * y1
    x1, y1 = x2, y2

a1 += x1 * yn
a2 += xn * y1


area = abs(a1 - a2) / 2
print(area)