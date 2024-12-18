text=open('day17.input').read().strip()
ta,tb,tc,_ = text.split('\n',3)
ra = int(ta.split(": ")[1])
rb = int(tb.split(": ")[1])
rc = int(tc.split(": ")[1])
program = [int(x.split()[-1]) for x in text.split('\n\n')[1].split(',')]
ip = 0 # instruction pointer
state_init = (ip, ra, rb, rc, program, [])

def read_combo(op, state):
    ip, ra, rb, rc, program, out = state
    if op <= 3:
        return op
    elif op == 4:
        return ra
    elif op == 5:
        return rb
    elif op == 6:
        return rc
    elif op == 7:
        raise Exception

def exe(state, debug=False):
    ip, ra, rb, rc, program, out = state
    
    opcode = program[ip]
    operand = program[ip+1]
    
    ip += 2
    
    if opcode == 0:
        # adv
        numerator = ra
        denominator = 2 ** read_combo(operand, state)
        #print('adv', ra, '/', denominator)
        ra = numerator // denominator
        if debug:
            print('adv', 'op', operand, 'ra', ra)
    
    elif opcode == 1:
        # bxl
        rb = rb ^ operand
        if debug:
            print('bxl', 'op', operand, 'rb', rb)
    elif opcode == 2:
        # bst
        rb = read_combo(operand, state) % 8
        if debug:
            print('bst', 'op', operand, 'rb', rb)
    elif opcode == 3:
        # jnz
        if debug:
            print('jnz', ra)
        if ra == 0:
            pass
        else:
            ip = operand
    elif opcode == 4:
        # bxc
        rb = rb ^ rc
        if debug:
            print('bxc', 'rb', rb, 'rc', rc)
    elif opcode == 5:
        # out
        if debug:
            print('out: op', operand, ra, rb, rc)
        out.append(read_combo(operand, state) % 8)
    elif opcode == 6:
        
        # bdv
        numerator = ra
        denominator = 2 ** read_combo(operand, state)
        #print('bdv', ra, '/', denominator)
        rb = numerator // denominator
        if debug:
            print('bdv', 'rb', rb)
    elif opcode == 7:
        
        # cdv
        numerator = ra
        denominator = 2 ** read_combo(operand, state)
        #print('cdv', ra, '/', denominator)
        rc = numerator // denominator
        if debug:
            print('cdv', 'op', operand, 'rc', rc)
    return ip, ra, rb, rc, program, out

M = [6, 7, 5, 6, 2, 3, 0, 1, 7, 5, 1, 6, 2, 3, 0, 1, 4]
magic = [0] * 8
for k in range(8):
    for i in range(len(M)):
        if M[i] == k:
            magic[k] = i
            break

def simulate(state):
    for i in range(100000):
        state = exe(state)
        cip, _ra, _rb, _rc, cpc, _ = state
        if cip >= len(cpc):
            break
    return state

def find_k(idx, target, state):
    ip, _, rb, rc, program, _ = state
    for k in range(100):
        ns = simulate((ip, 8**idx*k + 2**32, rb, rc, program, []))
        print(ns)
        if ns[-1][idx] == target:
            return k

print('part1', ','.join([str(x) for x in simulate((ip, ra, rb, rc, program, []))[-1]]))


def get_mul(X):
    t = 0
    for i in range(16):
        t += 8**i * X[i]
    return t

t = 0
N = 16
k = N-1
mul = [0] * 16
while k >= 0:
    for i in range(100):
        ns = simulate((ip, get_mul(mul) + 8**15, rb, rc, program, []))
        #print(ns)
        if ns[-1][k] == program[k]:
            break
        mul[k] += 1

    if i == 100:
        # should not try so many times
        error
        
    # check if break right digits
    br = False
    for j in range(k+1, N):
        if ns[-1][j] != program[j]:
            # reset
            br = True
            #print('breat at ', j, 'out', ns[-1])
            break
    if br:
        for p in range(j):
            mul[p] = 0
        mul[j] += 1
        # fix k+1 digit
        k = k + 1
    else:
        k -= 1
print('part_2', get_mul(mul) + 8**15)
