from itertools import permutations

def operate(a, b, op):
    """주어진 연산자에 따라 두 숫자를 계산하는 함수"""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def calculate(expression, ops):
    """연산자 우선순위에 따라 수식을 계산하는 함수"""
    # 숫자와 연산자 분리
    tmp = ""
    numbers = []
    operations = []
    for char in expression:
        if char.isdigit():
            tmp += char
        else:
            numbers.append(int(tmp))
            operations.append(char)
            tmp = ""
    numbers.append(int(tmp))
    
    # 연산자 우선순위에 따라 계산
    for op in ops:
        stack_num = []
        stack_op = []
        stack_num.append(numbers[0])
        for i in range(len(operations)):
            if operations[i] == op:
                stack_num.append(operate(stack_num.pop(), numbers[i+1], op))
            else:
                stack_num.append(numbers[i+1])
                stack_op.append(operations[i])
        numbers = stack_num[:]
        operations = stack_op[:]
    
    return abs(numbers[0])

def solution(expression):
    """우승 시 받을 수 있는 가장 큰 상금 금액을 반환하는 함수"""
    max_result = 0
    # 가능한 모든 연산자의 우선순위 조합 생성
    operations = ['+', '-', '*']
    for ops in permutations(operations, 3):
        # 각 우선순위 조합에 대한 결과값 계산
        result = calculate(expression, ops)
        # 최대값 갱신
        if result > max_result:
            max_result = result
    return max_result