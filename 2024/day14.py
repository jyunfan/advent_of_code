def get_case(line):
    left, right = line.split()
    init = left.split('=')[1].split(',')
    move = right.split('=')[1].split(',')
    return (int(init[0]),int(init[1])), (int(move[0]),int(move[1]))

def go(init, move, n, X, Y):
    x, y = init
    dx, dy = move
    tx = (x + dx * n) % X
    ty = (y + dy * n) % Y
    return tx, ty

lines = open('day14.input').read().strip().split('\n')
robots = [get_case(line) for line in lines]

#X = 11
#Y = 7
X = 101
Y = 103

def quadrant(x, y, X, Y):
    x += 1
    y += 1
    mX = (X+1)//2
    mY = (Y+1)//2
    if x == mX or y == mY:
        return 0
    if x < mX and y < mY:
        return 1
    elif x < mX and y > mY:
        return 2
    elif x > mX and y < mY:
        return 3
    elif x > mX and y > mY:
        return 4

K = 100
npos = [go(robot[0], robot[1], K, X, Y) for robot in robots]

Q = [0] * 5
for pos in npos:
    q = quadrant(pos[0], pos[1], X, Y)
    Q[q] += 1

print('part_1', Q[1]*Q[2]*Q[3]*Q[4])

input()

# draw
def show(pic):
    for row in pic:
        print(''.join([c+c for c in row]))

for k in range(0, 12):
    print(k)
    pic = [[' ']*X for x in range(Y)]
    npos = [go(robot[0], robot[1], k, X, Y) for robot in robots]
    for pos in npos:
        pic[pos[1]][pos[0]] = '*'
    show(pic)
    input()

# I found after 11 iteration, some thing special appears. And the pattern appear every 101 times.
# I tried check 11, 11+101, 11+101*2 and finally found 7687.
