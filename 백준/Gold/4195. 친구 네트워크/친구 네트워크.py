import collections
import sys




def union(a, b):
    a_root, b_root = find(a), find(b)
    if a_root != b_root:
        network[b_root] = a_root
        size[a_root] += size[b_root]  # 부모 노드의 사이즈를 업데이트합니다.


def find(a):
    while a != network[a]:
        network[a] = network[network[a]]  # 경로 압축
        a = network[a]
    return a


# 이제 count 함수는 O(1) 시간 안에 결과를 리턴합니다.
def count(a):
    return size[find(a)]


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    network = dict()
    size = collections.defaultdict(int)  # 각 집합의 크기를 추적하기 위한 사전

    for _ in range(N):
        a, b = sys.stdin.readline().strip().split()
        if a not in network:
            network[a] = a
            size[a] = 1
        if b not in network:
            network[b] = b
            size[b] = 1
        union(a, b)
        print(count(a))