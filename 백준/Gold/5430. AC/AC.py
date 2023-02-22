from collections import deque

T = int(input())
for _ in range(1, T + 1):
    cmd = input()
    M = len(cmd)
    N = int(input())
    st = input().lstrip('[').rstrip(']')
    st = deque(st.split(','))

    def func(N):
        i = 0
        while i < M:
            if cmd[i] == 'D':
                if N > 0:
                    st.popleft()
                    N -= 1
                else:
                    print('error')
                    return
            if cmd[i] == 'R':
                j = i + 1
                while j < M and cmd[j] != 'R':
                    j += 1
                if j == M:
                    st.reverse()
                    for _ in range(j - 1 - i):
                        if N > 0:
                            st.popleft()
                            N -= 1
                        else:
                            print('error')
                            return
                # j 가 R 에서 끝나는 경우. ex) RDDDDR. i = 0, j = 5
                elif cmd[j] == 'R':
                    for _ in range(j - 1 - i):
                        if N > 0:
                            st.pop()
                            N -= 1
                        else:
                            print('error')
                            return
                i = j
            i += 1
        print('[', end='')
        print(','.join(st), end='')
        print(']')
        return

    func(N)