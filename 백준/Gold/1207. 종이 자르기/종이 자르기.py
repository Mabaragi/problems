import sys
from copy import deepcopy

L = int(sys.stdin.readline().strip())

ground = [['.'] * L for _ in range(L)]

counter = 0
papers = []
for c in range(5):
    N, M = map(int, sys.stdin.readline().strip().split())
    paper = [list(sys.stdin.readline().strip()) for _ in range(N)]
    for i in paper:
        counter += i.count('#')
    papers.append([paper, c + 1])


papers.sort(key=lambda x: len(x[0]) * len(x[0][0]), reverse=True)


# for i in papers:
#     print(i)


def dfs(d):
    global ground
    curr_ground = deepcopy(ground)
    if d == 5:
        st = ''
        for i in ground:
            st += ''.join(i) + '\n'
        ans.append(st)
        return
    paper, cnt = papers[d]
    N = len(paper)
    M = len(paper[0])
    for i in range(L + 1 - N):
        for j in range(L + 1 - M):
            if set_paper(paper, i, j, cnt):
                dfs(d + 1)
            ground = deepcopy(curr_ground)


def set_paper(paper, i, j, counter):
    N = len(paper)
    M = len(paper[0])
    for r in range(N):
        for c in range(M):
            if paper[r][c] == '#':
                if ground[i + r][j + c] == '.':
                    ground[i + r][j + c] = str(counter)
                else:
                    # print('불가능')
                    return False
    return True


ans = []

if counter == L ** 2:
    dfs(0)

ans.sort()
if ans:
    print(ans[0].rstrip())
else:
    print('gg')
