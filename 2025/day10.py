import sys

inputs = sys.stdin.readlines()

def convert_buttons_to_int(buttons):
    print('buttons', buttons)
    nums = buttons[1:-1].split(',')
#    print(nums)
    return sum([2**int(x) for x in nums if x])

def convert_buttons_to_array(buttons, N):
    A = [0] * N
    nums = buttons[1:-1].split(',')
    for num in nums:
        A[int(num)] = 1
    return A

def parse_input(input):
    # treat target as binary string and convert to int
    target = int(input.split(']')[0][1:][::-1].replace('.','0').replace('#','1'), 2)
    # treat numbers as an integer
    numbers = [convert_buttons_to_int(x) for x in input.split(']')[1].split('{')[0].strip().split(' ')]
    voltages = [int(x) for x in input.split('{')[1][:-2].split(',')]
    N = len(voltages)
    A = [convert_buttons_to_array(x, N) for x in input.split(']')[1].split('{')[0].strip().split(' ')]
    return target, numbers, voltages, A

def trace(target, pos, numbers, visited):
    min_steps = 99999
    for number in numbers[pos:]:
        if number in visited:
            continue
        visited.add(number)
        if target == number:
            #print('found', visited)
            min_steps = min(min_steps, len(visited))
            #print('min_steps', min_steps)
        steps = trace(target ^ number, pos+1, numbers, visited)
        min_steps = min(min_steps, steps)
        visited.remove(number)
    return min_steps

ans = 0
for input in inputs:
    target, numbers, voltages, A = parse_input(input)
    print(target, numbers, voltages)
    s = trace(target, 0, numbers, set())
    ans += s
print('part 1:', ans)

from ortools.sat.python import cp_model

def solve_min_sum_integer(A, B):
    M = len(A)      # x 的長度
    N = len(B)

    model = cp_model.CpModel()

    # 1. 變數 x_i >= 0, 整數
    # 這裡上界先給一個適當值，例如 0~100000
    x = [model.NewIntVar(0, 100000, f'x_{i}') for i in range(M)]

    # 2. 約束：A^T x = B   （對每一個 j：sum_i A[i][j] * x_i == B[j]）
    for j in range(N):
        model.Add(
            sum(A[i][j] * x[i] for i in range(M)) == B[j]
        )

    # 3. 目標：min sum(x_i)
    model.Minimize(sum(x))

    # 4. 解
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = [solver.Value(v) for v in x]
        return solution, solver.ObjectiveValue()
    else:
        return None, None

ans_part2 = 0
for input in inputs:
    target, numbers, voltages, A = parse_input(input)
    print(target, 'voltages', voltages, 'A', A)
    ans = solve_min_sum_integer(A, voltages)
    ans_part2 += ans[1]
    print('ans', ans)
print('part 2:', ans_part2)