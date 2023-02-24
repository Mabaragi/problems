import sys

import heapq

T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    mn_heap = []
    mx_heap = []
    elems = 0
    for _ in range(N):
        cmd, num = sys.stdin.readline().split()
        num = int(num)
        common_append = [num, True]
        if cmd == 'I':
            heapq.heappush(mn_heap, [common_append])
            heapq.heappush(mx_heap, [-num, common_append])
            elems += 1
        else:
            if elems == 0:
                continue
            if num == 1:
                while True:
                    element = heapq.heappop(mx_heap)
                    if element[1][1] == False:
                        continue
                    else:
                        element[1][1] = False
                        break
                elems -= 1
            else:
                while True:
                    element = heapq.heappop(mn_heap)
                    if element[0][1] == False:
                        continue
                    else:
                        element[0][1] = False
                        break
                elems -= 1
    answer = []
    if elems == 0:
        print('EMPTY')

    else:
        for i in mx_heap:
            if i[1][1] == True:
                answer.append(i[1][0])
        for i in mn_heap:
            if i[0][1] == True:
                answer.append(i[0][0])

        print(max(answer), min(answer))