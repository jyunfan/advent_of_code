import sympy as sp
text = open('day13.input').read().strip().split('\n\n')

def get_case1(text):
    lines = text.split('\n')
    a1 = int(lines[0].split('X+')[1].split(',')[0])
    a2 = int(lines[0].split('Y+')[1].split(',')[0])
    b1 = int(lines[1].split('X+')[1].split(',')[0])
    b2 = int(lines[1].split('Y+')[1].split(',')[0])
    t1 = int(lines[2].split('X=')[1].split(',')[0])
    t2 = int(lines[2].split('Y=')[1].split(',')[0])
    return a1, a2, b1, b2, t1, t2

def get_case2(text):
    lines = text.split('\n')
    a1 = int(lines[0].split('X+')[1].split(',')[0])
    a2 = int(lines[0].split('Y+')[1].split(',')[0])
    b1 = int(lines[1].split('X+')[1].split(',')[0])
    b2 = int(lines[1].split('Y+')[1].split(',')[0])
    t1 = int(lines[2].split('X=')[1].split(',')[0])+10000000000000
    t2 = int(lines[2].split('Y=')[1].split(',')[0])+10000000000000
    return a1, a2, b1, b2, t1, t2

def solve(param):
    a1, a2, b1, b2, t1, t2 = param
    
    # special check
    if a1 * b2 == a2 * b1:
        raise Exception("special case")
        
    
    x, y = sp.symbols('x y')

    equation1 = sp.Eq(a1 * x + b1 * y, t1)
    equation2 = sp.Eq(a2 * x + b2 * y, t2)

    solution = sp.solve((equation1, equation2), (x, y))

    return solution[x], solution[y]

tokens = 0
for case in [get_case1(x) for x in text]:
    x, y = solve(case)
    if x != int(x) or y != int(y):
        continue
    tokens += 3 * x + y
print('part1', tokens)

tokens = 0
for case in [get_case2(x) for x in text]:
    x, y = solve(case)
    if x != int(x) or y != int(y):
        continue
    tokens += 3 * x + y
print('part2', tokens)
