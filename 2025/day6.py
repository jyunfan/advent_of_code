import sys
import numpy as np

inputs = [x.strip('\n') for x in sys.stdin.readlines()]

nums = []
for i in range(len(inputs)-1):
    nums.append(inputs[i].split())
nums = np.array(nums).astype(int)
op = inputs[len(inputs)-1].split()

print(op, nums)

def value(A, op):
    return np.sum(A) if op == '+' else np.prod(A)
part_ans = sum(value(nums[:, col], op[col]) for col in range(nums.shape[1]))

print('part 1:', part_ans)

# part 2
# transpose 2D array inputs

A = np.array([list(x) for x in inputs]).T
op = ''
ans = 0
block = []
last_row = False
for i, row in enumerate(A):
    if i == len(A) - 1:
        last_row = True
    v = 0
    print(row)
    for c in row:
        if c >= '1' and c <= '9':
            v = v * 10 + int(c)
        elif c == '*':
            op = '*'
        elif c == '+':
            op = '+'
    if v > 0:
        block.append(v)
    print(v, op)
    if v == 0 or last_row:  # end of block
        if op == '+':
            block_v = sum(block)
        else:
            block_v = np.prod(block)
        ans += block_v
        print('block', block, 'op', op, 'block_v', block_v, 'ans', ans)
        block = []
print('part 2:', ans)
    