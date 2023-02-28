N = int(input())
R = []
G = []
B = []
for _ in range(N):
    a, b, c = map(int,input().split())
    R.append(a)
    G.append(b)
    B.append(c)
red_cost = [0] * N
blue_cost = [0] * N
green_cost = [0] * N
red_cost[0] = R[0]
green_cost[0] = G[0]
blue_cost[0] = B[0]
for i in range(1, N):
    red_cost[i] = min(green_cost[i - 1], blue_cost[i - 1]) + R[i]
    green_cost[i] = min(red_cost[i - 1], blue_cost[i - 1]) + G[i]
    blue_cost[i] = min(green_cost[i - 1], red_cost[i - 1]) + B[i]

print(min(red_cost[N-1], blue_cost[N-1], green_cost[N-1]))