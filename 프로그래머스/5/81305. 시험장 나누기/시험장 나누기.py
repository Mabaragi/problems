# parametric search. 누적합을 구한뒤에, middle 값을 초과하면 counter 추가.
import sys
sys.setrecursionlimit(20000)

sm = [0] * 10000
counter = 1
def dfs(node, links, num, key):
    global counter
    left_node, right_node = links[node]
    left_value = dfs(left_node, links, num, key) if left_node != -1 else 0
    right_value = dfs(right_node, links, num, key) if right_node != -1 else 0
    if key >= left_value + right_value + num[node]:
        sm[node] = left_value + right_value + num[node]
    # elif left_value + num[node] <= key < left_value + right_value + num[node]:
    #     # print(f'cut : {node}, {right_node}')
    #     sm[node] = left_value + num[node]
    #     counter += 1
    # elif right_value + num[node] <= key < left_value + right_value + num[node]:
    #     # print(f'cut : {node}, {left_node}')
    #     sm[node] = right_value + num[node]
    #     counter += 1
    elif left_value + num[node] <= key or right_value + num[node] <= key:
        # print(f'cut : {node}, {right_node}')
        sm[node] = min(left_value, right_value) + num[node]
        counter += 1
    elif key < left_value + num[node] or key < right_value + num[node]:
        # print(f'cut : {node}, {left_node}, {right_node}')
        sm[node] = num[node]
        counter += 2
    
    return sm[node]
    
    

def solution(k, num, links):
    global counter
    N = len(num)
    
    # 루트노드 찾기
    in_degree = [0] * N
    for left, right in links:
        if left != -1:
            in_degree[left] += 1
        if right != -1:
            in_degree[right] += 1
    for i in range(N):
        if in_degree[i] == 0:
            start = i
            break
    left, right = max(num), sum(num)
    answer = sum(num)
    while left <= right:
        middle = (left + right) // 2            
        counter = 1
        dfs(start, links, num, middle)
        if counter > k:  #
            left = middle + 1
        else:
            answer = middle
            right = middle - 1
            
    
    return answer