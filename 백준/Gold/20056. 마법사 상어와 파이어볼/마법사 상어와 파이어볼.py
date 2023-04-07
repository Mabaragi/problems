from collections import defaultdict

N, M, K = map(int, input().split())
fire_balls = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_balls.append([r - 1, c - 1, m, s, d])
drc = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
for _ in range(K):
    next_fireballs = defaultdict(list)
    for fire_ball in fire_balls:
        r, c, m, s, d = fire_ball
        dr, dc = drc[d]
        nr, nc = (r + s * dr) % N, (c + s * dc) % N
        next_fireballs[nr, nc].append([nr, nc, m, s, d])
    fire_balls = []
    for r, c in next_fireballs:
        if len(next_fireballs[r, c]) >= 2:
            nm = 0
            ns = 0
            all_odd = all_even = True
            for fire_ball in next_fireballs[r, c]:
                *head, m, s, d = fire_ball
                if d % 2 == 0:
                    all_odd = False
                else:
                    all_even = False
                nm += m
                ns += s
            nm = nm // 5
            if nm == 0:
                continue
            ns = ns // len(next_fireballs[r, c])
            if all_odd or all_even:
                fire_balls.extend([[r, c, nm, ns, d] for d in range(0, 8, 2)])
            else:
                fire_balls.extend([[r, c, nm, ns, d] for d in range(1, 8, 2)])
        else:
            fire_balls.append(next_fireballs[r, c][0])
print(sum([i[2] for i in fire_balls]))