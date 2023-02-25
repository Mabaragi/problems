N = int(input())
trilst = [list(map(int, input().split())) for _ in range(N)]

trilst2 = [[0] * (i + 1) for i in range(N)]
trilst2[0][0] = trilst[0][0]

for i in range(1, N):
    trilst2[i][0] = trilst2[i - 1][0] + trilst[i][0]
    trilst2[i][i] = trilst2[i - 1][i - 1] + trilst[i][i]
    for j in range(1, i):
        trilst2[i][j] = max(trilst2[i - 1][j - 1], trilst2[i - 1][j]) + trilst[i][j]

trilst2[0][0] = trilst[0][0]

print(max(trilst2[N-1]))